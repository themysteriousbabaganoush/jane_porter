# filename: interactive_http_server.py

import http.server
import socketserver
import cgi
import os
import socket

UPLOAD_DIR = "uploads"

# Get your local IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html = """
                <html><body>
                <h2>File Upload Portal</h2>
                <form enctype="multipart/form-data" method="post">
                <input name="file" type="file"/>
                <input type="submit" value="Upload"/>
                </form>
                <hr>
                <h3>📂 Files in Current Directory</h3>
                <ul>
            """

            for item in os.listdir("."):
                if os.path.isdir(item):
                    html += f'<li><a href="{item}/">{item}/</a></li>'
                else:
                    html += f'<li><a href="{item}">{item}</a></li>'

            html += """
                </ul>
                <hr>
                <a href="/uploads/">View Uploaded Files Only</a>
                </body></html>
            """

            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()



    def do_POST(self):
        client_ip = self.client_address[0]
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype != 'multipart/form-data':
            self.send_error(400, "Bad Request")
            return

        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        pdict['CONTENT-LENGTH'] = int(self.headers.get('content-length'))
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                environ={'REQUEST_METHOD': 'POST'},
                                keep_blank_values=True)

        if 'file' not in form:
            self.send_error(400, "No file field found")
            return

        upload_file = form['file']
        filename = os.path.basename(upload_file.filename)
        file_data = upload_file.file.read()
        file_size_kb = round(len(file_data) / 1024, 2)

        print(f"\n🔔 Upload request from {client_ip}")
        print(f"📄 File: {filename}")
        print(f"📦 Size: {file_size_kb} KB")
        allow = input("Accept upload? (y/n): ").strip().lower()

        if allow != 'y':
            self.send_response(403)
            self.end_headers()
            self.wfile.write("❌ Upload denied by server.".encode('utf-8'))
            print("🚫 Upload denied.\n")
            return

        os.makedirs(UPLOAD_DIR, exist_ok=True)
        with open(os.path.join(UPLOAD_DIR, filename), 'wb') as f:
            f.write(file_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write("✅ Upload successful.".encode('utf-8'))
        print("✅ File uploaded and saved.\n")

# Allow port selection
def choose_port():
    print("📡 Scanning for available ports...\n")
    available_ports = []
    for p in range(1024, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', p)) != 0:
                available_ports.append(p)
        if len(available_ports) == 10:
            break

    for idx, port in enumerate(available_ports, 1):
        print(f"[{idx}] Port {port}")

    choice = input("\nChoose a port by number or type your own (default 7777): ").strip()
    if choice.isdigit():
        i = int(choice)
        if 1 <= i <= len(available_ports):
            return available_ports[i - 1]
        elif 1024 <= i <= 65535:
            return i
    return 7777

# Start the server
def start_server(port=7777):
    ip = get_local_ip()
    print(f"\n🚀 Server running at: http://{ip}:{port}/")
    print("📁 Uploads will be saved in: ./uploads/\n")
    os.chdir('.')  # Serve current dir (including /uploads/)
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped.")

# Entry point
if __name__ == "__main__":
    selected_port = choose_port()
    start_server(selected_port)

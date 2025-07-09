
# 📦 interactive_http_server.py

> ⚔️ **Turn your machine into a mini file-sharing fortress** — with interactive uploads, port scanning, and old-school terminal charm.

---

Sha 256 sums

0165766f9258f02ad3074daf7162b0055df835a219205edb05c7535b43e5eec6  jane_porter
4675ac85fb71ea118b8c42a4fa68043b006ccccc3b51565cd47f9933768cb250  jane_porter.py
0421a338fd1bfa8cdf7abaeffd031ae06a59cd3431085a7503aceac5995ed724  jane_porters_window.exe

---

## 🚀 **What is this?**

A Python-powered HTTP server that:
- Hosts files in the current directory over HTTP
- Lets anyone upload files through a browser (but **asks you first!**)
- Lists your directory and uploads folder neatly
- Scans & suggests 10 available ports, so you never fight for a busy one
- Shows your local IP + port for easy sharing

All in one **standalone script**.

---

## 🧰 **Features**
✅ Runs on Linux, Windows, macOS  
✅ Upload confirmation: *"Accept upload? (y/n)"* — you stay in control  
✅ Neat HTML interface (simple, but works)  
✅ Saves uploads to `./uploads/`  
✅ Cross-platform, Python 3  
✅ Can be bundled into a single EXE/ELF with `pyinstaller` — runs without Python!

---

## ⚙️ **Usage**

```bash
python3 interactive_http_server.py
```

- Script will scan & suggest free ports:
  ```
  📡 Scanning for available ports...

  [1] Port 5023
  [2] Port 5030
  ...
  Choose a port by number or type your own (default 7777):
  ```
- Visit the address shown, e.g.:
  ```
  🚀 Server running at: http://192.168.1.42:5023/
  📁 Uploads will be saved in: ./uploads/
  ```

- Upload files via browser.  
- On each upload, the terminal asks:
  ```
  🔔 Upload request from 192.168.1.50
  📄 File: secrets.txt
  📦 Size: 2.45 KB
  Accept upload? (y/n):
  ```

---

## 📦 **Build as a standalone EXE (Windows)**

```bash
pip install pyinstaller
pyinstaller --onefile interactive_http_server.py
```

Creates:
```
dist/interactive_http_server.exe
```

Now you can run it **without Python** on any Windows machine.

*For Linux, build on Linux to get a native ELF.*

---

## 🧙 **Why?**

Because sometimes you need:
- Quick file drops to your laptop
- Sharing files on LAN without setting up Apache or Nginx
- Saying "yes" or "no" to uploads like a firewall with a human face

---

## ⚠️ **Disclaimer**

> 🧪 This is a fun, educational tool.
> Do **not** expose it to the internet.
> Use only on trusted networks.
> All responsibility for use is yours.

---

## ✨ **Made by Chairman Hellsing & Mun**
Crafted in the spirit of curiosity, code, and old kingdoms reborn.

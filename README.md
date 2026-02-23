# Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Nmap](https://img.shields.io/badge/Tool-Nmap-red)
![GUI](https://img.shields.io/badge/Interface-Tkinter-green)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A GUI-based port scanning tool built using Python and Tkinter, integrating Nmap for network reconnaissance and service detection in controlled lab environments.

---

## 🚀 Features

- Quick Scan (Top 1000 common ports)
- Full Port Scan (All 65,535 ports)
- Service Version Detection
- Real-time scan output display
- User-controlled report export
- Date & Time stamped scan reports
- Clean graphical interface

---

## 🛠️ Tech Stack

- Python  
- Tkinter (GUI Framework)  
- Nmap  
- Linux  

---

## 📦 Installation & Usage

### 1️⃣ Install Python

```bash
python3 --version
```

### 2️⃣ Install Nmap

```bash
sudo apt install nmap
```

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/aroh3006/Port-Scanner.git
cd Port-Scanner
```

### 4️⃣ Run the Application

```bash
python3 gui_scanner.py
```

---

## 🧠 How It Works

1. The user enters a target IP address or domain.  
2. The tool integrates Nmap to perform selected scan types.  
3. Scan results are displayed in real-time within the GUI.  
4. Users can export structured reports with automatic date and time stamping.  

---

## 📊 Scan Modes

| Mode | Description |
|------|------------|
| Quick Scan | Scans the top 1000 commonly used ports |
| Full Scan | Scans all 65,535 ports |
| Service Scan | Detects service versions running on open ports |

---

## 🔐 Security Concepts Implemented

- Network Reconnaissance  
- Port Enumeration  
- Service Version Detection  
- Information Gathering  
- Ethical Hacking Methodology  

---

## ⚠️ Disclaimer

This tool is intended strictly for educational purposes and authorized lab environments only.  
Do NOT use against systems without explicit permission.

---

## 📌 Future Improvements

- Progress bar for long scans  
- Multi-threaded scanning  
- Dark mode UI  
- PDF report export  
- CVE integration for vulnerability mapping  

---

## 👨‍💻 Author

**Aroh Maurya**  
GitHub: https://github.com/aroh3006  

---

⭐ If you found this useful, consider giving the repository a star.

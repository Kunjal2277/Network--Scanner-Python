# 🔍 Network Port Scanner

> A beginner-friendly Python network scanner built as part of my cybersecurity learning journey on TryHackMe.

**Author:** Kunjal Goyal | PEC Chandigarh | 1st Year Engineering Student  
**LinkedIn:** [linkedin.com/in/kunjal-g-188833375](https://www.linkedin.com/in/kunjal-g-188833375)

---

## 📌 What This Project Does

This tool scans a target IP address or hostname for **open ports**, identifies the **services running** on those ports, and provides a beginner-friendly **security risk analysis** — similar to how professional tools like Nmap work, but written from scratch in Python.

It also **auto-generates a scan report** saved as a `.txt` file.

---

## 🧠 What I Learned (From TryHackMe)

This project directly applies concepts from:
- ✅ **TryHackMe Pre-Security Path** — TCP/IP model, ports & protocols, how services communicate
- ✅ **TryHackMe Cybersecurity 101** — Common vulnerabilities, attack surfaces, risk assessment
- ✅ **Python scripting** — socket programming, file I/O, CLI design

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔎 Port scanning | Checks 18 common ports (or custom range) |
| 🏷️ Service detection | Identifies HTTP, SSH, FTP, RDP, SMB and more |
| 🔐 Risk analysis | Flags dangerous open ports with explanation |
| 🪧 Banner grabbing | Tries to identify service versions |
| 📄 Report generation | Saves results to a `.txt` file automatically |
| 🎯 3 scan modes | Quick / Standard / Custom port range |

---

## 🛠️ How to Run

**Requirements:** Python 3.x (no extra libraries needed — uses only built-in modules)

```bash
# Clone the repo
git clone https://github.com/Kunjal2277/network-scanner-python.git
cd network-scanner-python

# Run it
python3 scanner.py

# OR pass target directly
python3 scanner.py 192.168.1.1
```

---

## 📸 Sample Output

```
╔══════════════════════════════════════════════╗
║        🔍 NETWORK PORT SCANNER v1.0          ║
║        By Kunjal G. | PEC Chandigarh         ║
║        Inspired by TryHackMe Learning Path   ║
╚══════════════════════════════════════════════╝

  [✓] Target   : scanme.nmap.org
  [✓] IP       : 45.33.32.156
  [✓] Scanning : 18 ports
  [✓] Started  : 2026-06-28 14:32:10

────────────────────────────────────────────────────────────
  PORT     SERVICE              STATUS    
────────────────────────────────────────────────────────────
  22       SSH                  OPEN 🟢
  80       HTTP                 OPEN 🟢
  443      HTTPS                OPEN 🟢

  ✅ Scan complete in 4.2s
  📊 Open ports found: 3 / 18

  🔐 SECURITY ANALYSIS
  ──────────────────────────────────────────────────
  Port 22 (SSH)
  ✅ Low    — SSH is secure but brute-force is common

  Port 80 (HTTP)
  ⚠️  Medium — HTTP is unencrypted

  Port 443 (HTTPS)
  ✅ Low    — HTTPS is encrypted (check certificate!)

  💡 RECOMMENDATIONS
  ──────────────────────────────────────────────────
  • Close any ports you don't actively need
  • Always use HTTPS (443) instead of HTTP (80)

  📄 Report saved → scan_report_scanme_nmap_org_20260628_143214.txt
```

---

## ⚠️ Legal & Ethical Notice

> This tool is for **educational purposes only**.  
> Only scan systems and networks **you own** or have **explicit written permission** to test.  
> Unauthorized scanning is illegal and unethical.  
> Always practice on safe environments like [TryHackMe](https://tryhackme.com) labs or your own home network.

---

## 🧪 Safe Targets to Practice On

| Target | Notes |
|---|---|
| `127.0.0.1` | Your own localhost — always safe |
| `scanme.nmap.org` | Officially provided by Nmap for practice |
| Your home router IP | Usually `192.168.1.1` — safe on your own network |
| TryHackMe lab machines | Spin up rooms and scan the given IP |

---

## 📚 Concepts Behind The Code

| Python Concept | Used For |
|---|---|
| `socket` module | Creating TCP connections to test ports |
| `socket.connect_ex()` | Returns 0 if port is open, error code if closed |
| `settimeout()` | Prevents hanging on unresponsive ports |
| `datetime` module | Timestamps for reports |
| `sys.argv` | Accepting command-line arguments |
| File I/O | Writing scan reports to `.txt` |

---

## 🗺️ What's Next (Planned Improvements)

- [ ] Multi-threading for faster scanning
- [ ] UDP port scanning
- [ ] HTML report generation
- [ ] CVE lookup for identified services
- [ ] Export to JSON format

---

## 🤝 Connect With Me

I'm a 1st year student at PEC Chandigarh actively learning penetration testing and ethical hacking.

- 🔗 LinkedIn: [kunjal-g-188833375](https://www.linkedin.com/in/kunjal-g-188833375)
- 🧑‍💻 GitHub: [Kunjal2277](https://github.com/Kunjal2277)
- 🎯 TryHackMe: Completed Pre-Security + Cybersecurity 101 paths

---

*Built with 💙 as part of my cybersecurity learning journey*

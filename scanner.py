#!/usr/bin/env python3
"""
========================================
  Network Port Scanner
  Author : Kunjal Goyal
  GitHub : github.com/Kunjal2277
  College: PEC Chandigarh
  Purpose: Cybersecurity learning project
           inspired by TryHackMe Pre-Security
           & Cybersecurity 101 paths
========================================
"""

import socket
import datetime
import sys
import time

# ── Common ports and their service names ──────────────────────
COMMON_PORTS = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    80:  "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306:"MySQL",
    3389:"RDP (Remote Desktop)",
    5900:"VNC",
    8080:"HTTP-Alt",
    8443:"HTTPS-Alt",
}

# ── Risk levels for open ports ────────────────────────────────
RISK = {
    21:  "⚠️  Medium — FTP can expose files if misconfigured",
    22:  "✅ Low    — SSH is secure but brute-force is common",
    23:  "🔴 HIGH   — Telnet sends data in PLAINTEXT! Very risky",
    25:  "⚠️  Medium — SMTP can be abused for spam/relay",
    53:  "⚠️  Medium — DNS can be vulnerable to amplification attacks",
    80:  "⚠️  Medium — HTTP is unencrypted",
    110: "⚠️  Medium — POP3 can expose emails if unencrypted",
    135: "🔴 HIGH   — RPC is a common attack vector on Windows",
    139: "🔴 HIGH   — NetBIOS leaks system info",
    143: "⚠️  Medium — IMAP unencrypted version is risky",
    443: "✅ Low    — HTTPS is encrypted (check certificate!)",
    445: "🔴 HIGH   — SMB — famously exploited by EternalBlue/WannaCry",
    3306:"🔴 HIGH   — MySQL should NEVER be exposed to the internet",
    3389:"🔴 HIGH   — RDP is a top target for ransomware groups",
    5900:"🔴 HIGH   — VNC often has weak/no authentication",
    8080:"⚠️  Medium — Often used for dev servers, may be unpatched",
    8443:"✅ Low    — HTTPS alternate port",
}


def print_banner():
    print("""
╔══════════════════════════════════════════════╗
║        🔍 NETWORK PORT SCANNER v1.0          ║
║        By Kunjal Goyal | PEC Chandigarh      ║
║        Inspired by TryHackMe Learning Path   ║
╚══════════════════════════════════════════════╝
    """)


def resolve_host(target):
    """Resolve hostname to IP address."""
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"  [✗] Could not resolve host: {target}")
        sys.exit(1)


def scan_port(ip, port, timeout=1):
    """Try to connect to a port. Returns True if open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0  # 0 means connection successful = port OPEN
    except Exception:
        return False


def grab_banner(ip, port, timeout=1):
    """Try to grab service banner for extra info."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        # Return just the first line
        return banner.split("\n")[0][:60] if banner else None
    except Exception:
        return None


def scan_target(target, ports=None, timeout=1):
    """Main scanning function."""
    print_banner()

    # Resolve IP
    ip = resolve_host(target)
    print(f"  [✓] Target   : {target}")
    print(f"  [✓] IP       : {ip}")
    print(f"  [✓] Scanning : {len(ports)} ports")
    print(f"  [✓] Started  : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "─" * 60)
    print(f"  {'PORT':<8} {'SERVICE':<20} {'STATUS':<10}")
    print("─" * 60)

    open_ports = []
    start_time = time.time()

    for port in ports:
        service = COMMON_PORTS.get(port, "Unknown")
        is_open = scan_port(ip, port, timeout)

        if is_open:
            open_ports.append(port)
            banner = grab_banner(ip, port, timeout)
            banner_str = f"  ← {banner}" if banner else ""
            print(f"  {port:<8} {service:<20} {'OPEN 🟢':<10}{banner_str}")
        else:
            print(f"  {port:<8} {service:<20} {'closed':<10}", end="\r")

    elapsed = round(time.time() - start_time, 2)

    # ── Results Summary ───────────────────────────────────────
    print("\n" + "─" * 60)
    print(f"\n  ✅ Scan complete in {elapsed}s")
    print(f"  📊 Open ports found: {len(open_ports)} / {len(ports)}\n")

    if open_ports:
        print("  🔐 SECURITY ANALYSIS")
        print("  " + "─" * 50)
        for port in open_ports:
            service = COMMON_PORTS.get(port, "Unknown")
            risk    = RISK.get(port, "⚠️  Check this service manually")
            print(f"\n  Port {port} ({service})")
            print(f"  {risk}")

        print("\n\n  💡 RECOMMENDATIONS")
        print("  " + "─" * 50)
        print("  • Close any ports you don't actively need")
        print("  • Replace Telnet (23) with SSH (22) if open")
        print("  • Never expose MySQL (3306) or RDP (3389) publicly")
        print("  • Always use HTTPS (443) instead of HTTP (80)")
        print("  • Run this scan regularly to detect changes\n")
    else:
        print("  No open ports found — target appears well-secured! ✅\n")

    # ── Save report to file ───────────────────────────────────
    report_name = f"scan_report_{target.replace('.','_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_name, "w") as f:
        f.write(f"Network Scan Report\n")
        f.write(f"===================\n")
        f.write(f"Target  : {target}\n")
        f.write(f"IP      : {ip}\n")
        f.write(f"Date    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Scanner : Kunjal G. | github.com/Kunjal2277\n\n")
        f.write(f"Open Ports:\n")
        for port in open_ports:
            f.write(f"  - {port} ({COMMON_PORTS.get(port, 'Unknown')})\n")
        if not open_ports:
            f.write("  None found\n")
        f.write(f"\nScan Duration: {elapsed}s\n")

    print(f"  📄 Report saved → {report_name}\n")
    return open_ports


# ── Entry Point ───────────────────────────────────────────────
if __name__ == "__main__":

    print("\n  🔍 Network Port Scanner — by Kunjal G.")
    print("  ⚠️  Use only on networks/systems you OWN or have permission to scan!\n")

    # Get target
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("  Enter target IP or hostname: ").strip()

    # Scan mode
    print("\n  Select scan mode:")
    print("  [1] Quick scan — top 10 common ports")
    print("  [2] Standard scan — all 18 common ports (recommended)")
    print("  [3] Custom — enter your own port range")

    choice = input("\n  Your choice (1/2/3): ").strip()

    if choice == "1":
        ports = [22, 23, 80, 443, 445, 3306, 3389, 8080, 21, 25]
    elif choice == "3":
        start = int(input("  Start port: "))
        end   = int(input("  End port:   "))
        ports = list(range(start, end + 1))
    else:
        ports = list(COMMON_PORTS.keys())

    scan_target(target, ports=sorted(ports))

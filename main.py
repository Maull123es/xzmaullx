#!/usr/bin/env python3
import os
import socket
import csv
from datetime import datetime

# ===============================
#           ASCII LOGO
# ===============================
def print_logo():
    logo = r"""
╔══════════════════════════════════════════╗
║                                          ║
║   ███╗   ██╗███████╗██╗     ██╗   ██╗    ║
║   ████╗  ██║██╔════╝██║     ██║   ██║    ║
║   ██╔██╗ ██║█████╗  ██║     ██║   ██║    ║
║   ██║╚██╗██║██╔══╝  ██║     ██║   ██║    ║
║   ██║ ╚████║███████╗███████╗╚██████╔╝    ║
║   ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝     ║
║    info lebih lanjut dm ig @zxmaullx     ║
║         atau dm wa 085723375442          ║
║               made with love             ║
╚══════════════════════════════════════════╝
    """
    print(logo)

# ===============================
#            LOGGING
# ===============================
def save_log(filename, content):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    filepath = os.path.join("logs", filename)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"[+] Log saved to {filepath}")

# ===============================
#           CSV EXPORT
# ===============================
def save_csv(filename, headers, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"[+] CSV saved to {filename}")

# ===============================
#        IP/DOMAIN LOOKUP
# ===============================
def lookup_domain():
    target = input("Masukkan domain atau IP: ").strip()
    try:
        ip_address = socket.gethostbyname(target)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"Lookup Result:\nTarget: {target}\nIP Address: {ip_address}\nTime: {timestamp}"
        print(output)

        # Simpan log
        log_name = f"lookup_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        save_log(log_name, output)

        # Pilihan simpan ke CSV
        simpan_csv = input("Simpan ke CSV? (y/n): ").lower()
        if simpan_csv == "y":
            save_csv("output.csv", ["Target", "IP Address", "Timestamp"], [[target, ip_address, timestamp]])

    except socket.gaierror:
        print("[!] Gagal lookup. Periksa kembali domain/IP.")

# ===============================
#         MENU INTERAKTIF
# ===============================
def menu():
    while True:
        print_logo()
        print("1. Lookup Domain/IP")
        print("2. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            lookup_domain()
        elif pilihan == "2":
            print("Keluar...")
            break
        else:
            print("[!] Pilihan tidak valid.")

# ===============================
#        MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    menu()

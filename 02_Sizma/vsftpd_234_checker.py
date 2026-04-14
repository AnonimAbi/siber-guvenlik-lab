#!/usr/bin/env python3
# -- coding: utf-8 --
# Amaç: Hedefteki FTP servisinin vsftpd 2.3.4 (backdoor'lu) olup olmadığını kontrol edeceğiz.
# Kullanım: python3 vsftpd_234_checker.py <hedef_ip>

import socket
import sys

def check_vulnerability(ip, port=21):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        
        if "vsFTPd 2.3.4" in banner:
            print(f"[!] HEDEF SAVUNMASIZ: {banner}")
            print("[!] Bu sistem Metasploit vsftpd_234_backdoor modülü ile sızılabilir.")
            return True
        else:
            print(f"[*] Hedef güvenli veya farklı servis: {banner}")
            return False
    except Exception as e:
        print(f"[-] Bağlantı hatası: {e}")
        return False

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print(f"Kullanım: {sys.argv[0]} <hedef_ip>")
        sys.exit(1)
    check_vulnerability(sys.argv[1])

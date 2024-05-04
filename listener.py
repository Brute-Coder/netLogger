import socket 
import threading

# socket.gethostbyname(socket.gethostname())
SERVERIP = "192.168.31.173"
PORT = 12345
ADDR = (SERVERIP,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")
    msg = conn.recv(4096).decode('utf-8')
    print(f"[{addr}] ---> {msg}")
    print(f"[DISCONNECTED] {addr}")
    conn.close()

def start():
    server.listen()
    print(f"[ LISTENING] Server is listening on {SERVERIP}")
    while True :
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f" [ACTIVE CONNECTIONS] {threading.active_count()-1}")

    


print("[SERVER] is Starting.....")
start()
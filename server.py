import socket
import threading

def handle_client(conn, addr):
    try:
        print('Подключение клиента', addr)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Прием данных от клиента {}: {}'.format(addr, data.decode()))
            conn.sendall(data)
            
    except socket.error as e:
        print(f"Ошибка при работе с клиентом {addr}: {e}")
        
    finally:
        conn.close()
        print('Отключение клиента', addr)

def create_socket_and_listen():
    global sock
    sock = socket.socket()
    sock.bind(('', 9099))
    sock.listen(5)
    print('Начало прослушивания порта')

    while True:
        conn, addr = sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

create_socket_and_listen()

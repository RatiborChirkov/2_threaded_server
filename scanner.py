import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            return port
        sock.close()
    except:
        pass

def progress_bar(total, scanned):
    percent = (scanned / total) * 100
    print(f"Прогресс: [{int(percent)}%]", end='\r')

def main():
    host = input("Введите имя хоста/IP-адрес: ")
    open_ports = []
    total_ports = 65535

    scanned_ports = 0
    for port in range(1, total_ports + 1):
        scanned_ports += 1
        progress_bar(total_ports, scanned_ports)
        port_result = scan_port(host, port)
        if port_result:
            open_ports.append(port_result)
    
    print("\nОткрытые порты:", sorted(open_ports))

if __name__ == "__main__":
    main()

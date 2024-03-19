import socket

def connect_to_server():
    global sock
    sock = socket.socket()
    try:
        sock.connect(('localhost', 9099))
        print("Успешно подключено к серверу.")
    except socket.error as e:
        print(f"Ошибка при подключении к серверу: {e}")
        exit()

def send_data():
    try:
        message = input("Введите сообщение для отправки на сервер: ")
        print('Отправка данных серверу:', message)
        sock.sendall(message.encode())
        data = sock.recv(1024)
        print('Прием данных от сервера:', data.decode())
    except socket.error as e:
        print(f"Ошибка при отправке/получении данных: {e}")

def ex():
    exit()

connect_to_server()

options = {
    '1': send_data,
    '2': ex
}

while True:
    print("Меню:")
    print("1. Отправить данные серверу и получить ответ")
    print("2. Завершить программу")
    choice = input("Выберите действие: ")

    if choice in options:
        options[choice]()
    else:
        print("Неверный выбор. Пожалуйста, введите корректное значение.")

import socket
import time

# Configurações do cliente
HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

# Inicializa o relógio lógico com valor zero
clock = 0

# Cria o socket do cliente e conecta ao servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Envia a mensagem para o servidor
    value = input('Digite o valor para atualizar o relógio: ')
    client_socket.send(value.encode())

    # Recebe a resposta do servidor e atualiza o relógio
    data = client_socket.recv(BUFFER_SIZE)
    clock = int(data.decode())
    print(f'Recebido do servidor: {data.decode()} - Relógio: {clock}')

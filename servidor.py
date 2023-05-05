import socket
import time

# Configurações do servidor
HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

# Inicializa o relógio lógico com valor zero
clock = 0

# Cria o socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f'Servidor iniciado em {HOST}:{PORT}')

    # Aguarda a conexão de dois clientes
    conn1, addr1 = server_socket.accept()
    print(f'Cliente 1 conectado: {addr1}')
    conn2, addr2 = server_socket.accept()
    print(f'Cliente 2 conectado: {addr2}')

    # Processa as mensagens enviadas pelos clientes
    while True:
        # Recebe a mensagem do primeiro cliente e atualiza o relógio
        data1 = conn1.recv(BUFFER_SIZE)
        if not data1:
            break
        clock = max(clock, int(data1)) + 1
        print(f'Recebido do Cliente 1: {data1.decode()} - Relógio: {clock}')

        # Recebe a mensagem do segundo cliente e atualiza o relógio
        data2 = conn2.recv(BUFFER_SIZE)
        if not data2:
            break
        clock = max(clock, int(data2)) + 1
        print(f'Recebido do Cliente 2: {data2.decode()} - Relógio: {clock}')

        # Envia o valor atualizado do relógio para os dois clientes
        conn1.send(str(clock).encode())
        conn2.send(str(clock).encode())

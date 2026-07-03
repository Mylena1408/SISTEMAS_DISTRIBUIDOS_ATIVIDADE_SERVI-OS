import socket

HOST = "127.0.0.1"
PORTA = 6002


def registrar_evento(mensagem):

    print("[1] Criando socket...")

    cliente = socket.socket(...)

    print("[2] Definindo timeout...")

    cliente.settimeout(5)

    print("[3] Conectando na Auditoria...")

    print("Tentando conectar em:", HOST, PORTA)
    cliente.connect((HOST, PORTA))
    print("Conectou!")

    print("[4] Conectado!")

    cliente.send(mensagem.encode())

    print("[5] Mensagem enviada!")

    resposta = cliente.recv(1024).decode()

    print("[6] Resposta recebida!")

    cliente.close()

    return resposta
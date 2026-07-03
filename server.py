import socket #importa a biblioteca socket para criar o servidor TCP/IP#
from cliente_auditoria import registrar_evento

HOST = "127.0.0.1"
PORTA = 6001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORTA))

servidor.listen()

print("="*50)
print("SERVIÇO DE COBRANÇA")
print(f"Escutando em {HOST}:{PORTA}")
print("="*50)

while True:

    cliente, endereco = servidor.accept()

    print(f"\nCliente conectado: {endereco}")

    mensagem = cliente.recv(1024).decode()

    print("\nNova assinatura recebida")

    print(mensagem)
    
    print(">>> Iniciando comunicação com a Auditoria")

try:
    resposta_auditoria = registrar_evento(mensagem)
    print(">>> Resposta da Auditoria:", resposta_auditoria)

except Exception as erro:
    print(">>> ERRO AO CHAMAR A AUDITORIA:")
    print(type(erro).__name__)
    print(erro)

    cliente.send("Cobrança registrada com sucesso.".encode())

    cliente.close()
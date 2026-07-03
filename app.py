from flask import Flask, render_template, request
import socket

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/criar", methods=["POST"])
def criar():

    nome = request.form["nome"]
    plano = request.form["plano"]

    try:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        cliente.connect(("127.0.0.1", 6001))

        mensagem = f"""
Cliente: {nome}
Plano: {plano}
"""

        cliente.send(mensagem.encode())

        resposta = cliente.recv(1024).decode()

        cliente.close()

        print(resposta)

    except Exception as erro:

        print("Erro:", erro)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
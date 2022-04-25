from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    request = requests.get("http://localhost:3000")
    api = json.loads(request.content)
    return (api)


@app.route("/livros", methods=['GET'])
def listarLivros():
    request = requests.get("http://localhost:3000/livros")
    api = json.loads(request.content)
    return (api)


@app.route("/livros/busca", methods=['GET'])
def listarLivroPorEditora():
    request = requests.get("http://localhost:3000/livros/busca")
    api = json.loads(request.content)
    return (api)


@app.route("/livros/:id", methods=['GET'])
def listarLivroPorId():
    request = requests.get("http://localhost:3000/livros/:id")
    api = json.loads(request.content)
    return (api)


@app.route("/livros", methods=['POST'])
def cadastraLivro():
  pass


@app.route("/livros/:id", methods=['PUT'])
def atualizarLivro():
    pass


@app.route("/livros/busca", methods=['DELETE'])
def excluirLivro():
    pass


if __name__ == "__main__":
    app.run(debug=True)
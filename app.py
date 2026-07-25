import json
from flask import Flask, render_template, request, redirect
#Flask cria a aplicação web;
#render_template permite carregar arquivos HTML

#cria a aplicação
app = Flask(__name__)

def carregar_estoque():
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

#significa: Quando alguém acessar a página principal /, execute a função abaixo:
@app.route("/")
#manda o flask devolver o arquivo:
def inicio():
    produtos = carregar_estoque()
    return render_template("index.html", produtos=produtos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    codigo = request.form["codigo"].strip().upper()
    if len(codigo) > 6:
        return redirect("/")
    quantidade = request.form["quantidade"]
    quantidade = int(quantidade)
    produtos = carregar_estoque()
    produto = {
        "nome": nome,
        "id": codigo,
        "quantidade": quantidade
    }
    produtos.append(produto)
    salvar_estoque(produtos)
    return redirect("/")

def salvar_estoque(produtos): #agora a função recebe a lista que queremos salvar
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

@app.route("/remover/<codigo>", methods=["POST"])
def remover(codigo):
    produtos = carregar_estoque()

    for produto in produtos:
        if produto["id"] == codigo:
            produtos.remove(produto)
            salvar_estoque(produtos)
            break

    return redirect("/")                                        

if __name__ == "__main__":
    app.run(debug=True)
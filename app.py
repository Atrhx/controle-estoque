import json
from flask import Flask, render_template, request, redirect, flash
#Flask cria a aplicação web;
#render_template permite carregar arquivos HTML

#cria a aplicação
app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

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
        flash("O código deve ter no máximo 6 caracteres.", "erro")
        return redirect("/")
    try:
        quantidade = int(request.form["quantidade"])
        if quantidade < 0:
            flash("A quantidade não pode ser negativa", "erro")
            return redirect("/")
    except ValueError:
        flash("Digite uma quantidade válida!", "erro")
        return redirect("/")

    produtos = carregar_estoque()
    for produto in produtos:
        if produto["id"] == codigo:
            flash(f"O código {codigo} já está cadastrado.", "erro")
            return redirect("/")
    produto = {
        "nome": nome,
        "id": codigo,
        "quantidade": quantidade
    }
    produtos.append(produto)
    salvar_estoque(produtos)
    flash("Produto cadastrado com sucesso!", "sucesso")
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

@app.route("/editar/<codigo_original>", methods=["POST"])
def editar(codigo_original):
    nome = request.form["nome"].strip()
    novo_codigo = request.form["codigo"].strip().upper()

    try:
        quantidade = int(request.form["quantidade"])

        if quantidade < 0:
            flash("A quantidade não pode ser negativa.", "erro")
            return redirect("/")

    except ValueError:
        flash("Digite uma quantidade válida.", "erro")
        return redirect("/")

    if len(novo_codigo) > 6:
        flash("O código deve ter no máximo 6 caracteres.", "erro")
        return redirect("/")

    produtos = carregar_estoque()

    for produto in produtos:
        if produto["id"] == novo_codigo and produto["id"] != codigo_original:
            flash(f"O código {novo_codigo} já está cadastrado.", "erro")
            return redirect("/")
    for produto in produtos:
        if produto["id"] == codigo_original:
            produto["nome"] = nome
            produto["id"] = novo_codigo
            produto["quantidade"] = quantidade

            salvar_estoque(produtos)

            flash("Produto atualizado com sucesso!", "sucesso")
            return redirect("/")
        
    flash("Produto não encontrado.", "erro")
    return redirect("/")   

if __name__ == "__main__":
    app.run(debug=True)
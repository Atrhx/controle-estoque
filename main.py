import time
import json

def carregar_estoque():
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

produtos_estoque = carregar_estoque()

#Salvar arquivos em JSON
def salvar_estoque():
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos_estoque, arquivo, indent=4, ensure_ascii=False)

#Cadastra produto 
def cadastrar_produtos():
    descricao_produto = input("Descrição do item:") 
    # Verifica se o código já está cadastrado.
   
    while True:
            codigo = input("Código do item:")
            codigo_existe = False

            for produto in produtos_estoque:
                if produto["id"] == codigo:
                    codigo_existe =  True

            if codigo_existe:
                print("Esse código já está cadastrado.")
            else:
                break

    #Filtra para a quantidade só aceitar números positivos, não aceita negativos, ou por extenso (ex: "cinco").            
    while True: 
        try:
            quantidade = int(input("Quantidade:"))
            if quantidade < 0:
                print("Quantidade não pode ser negativa!")
            else: 
                break
        except ValueError:
            print("Quantidade inválida! Digite apenas números.")
    produto_cadastrado = {"nome": descricao_produto, "id": codigo, "quantidade": quantidade}
    produtos_estoque.append(produto_cadastrado)

def buscar_produto():
    encontrado = False
    codigo = input("Digite o código para busca: ")

    for produto in produtos_estoque:
        if produto["id"] == codigo:
            encontrado = True
            print("Código encontrado!")
            print("Descrição: ", produto["nome"])
            print("Quantidade: ", produto["quantidade"])
            break

    if not encontrado:
        print("Não encontrado")


def listar_produtos():
    for produto in produtos_estoque:
        print(f"Descrição: {produto['nome']}")
        print(f"ID: {produto['id']}")
        print(f"Quantidade: {produto['quantidade']}")

def atualizar_quantidade():
    encontrado = False
    codigo = input("Qual produto deseja atualizar a quantidade? (Inserir o código) ")
    for produto in produtos_estoque:
        if produto['id'] == codigo:
            encontrado = True
            print("Descrição: ", produto["nome"])
            print("Quantidade: ", produto["quantidade"])

            print("Você deseja: ")
            print("1. Atualizar quantidade")
            print("2. Sair")
            acao = input("Opção: ")
            if acao == "1":
                while True:
                    try:
                        nova_quantidade = int(input("Nova quantidade: "))
                        if nova_quantidade < 0:
                            print("Quantidade não pode ser negativa!")
                        else:
                            print("Salvando novo valor...")
                            produto["quantidade"] = nova_quantidade
                            print("Saindo...")
                            break
                    except ValueError:
                        print("Quantidade precisa ser um número válido!")
                break  
            elif acao == "2":
                break
            else:
                print("Ação inválida!")
    if not encontrado:
        print("Não encontrado")

def remover_produto():
    encontrado = False
    codigo = input("Qual produto deseja remover? (Inserir o código) ")

    for produto in produtos_estoque:
        if produto["id"] == codigo:
            encontrado = True

            print(f"Descrição: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")

            while True:
                acao = input("Deseja remover esse produto? (S/N) ").lower()

                if acao == "s":
                    produtos_estoque.remove(produto)
                    print("Produto removido com sucesso!")
                    break

                elif acao == "n":
                    print("Remoção cancelada.")
                    break

                else:
                    print("Ação inválida.")

            break

    if not encontrado:
        print("Produto não encontrado.")
while True:
    print("="*3, "CONTROLE DE ESTOQUE", "="*3)
    print("\n1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Procurar produto")
    print("4. Atualizar quantidade")
    print("5. Remover produto")
    print("6. Sair\n")
    print("="*28)
    acao = input("Escolha uma opção: ")

    if acao == "1":
        cadastrar_produtos()
    elif acao == "2":
        listar_produtos()
    elif acao == "3":
        buscar_produto()
    elif acao == "4":
        atualizar_quantidade()    
    elif acao == "5":
        remover_produto()
    elif acao == "6":
        salvar_estoque()
        print("Salvando os produtos")
        time.sleep(5)
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
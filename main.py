import time

produtos_estoque = []

def cadastrar_produtos():
    descricao_produto = input("Descrição do item:")
    codigo = input("Código do item:")
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

def listar_produtos():
    for produto in produtos_estoque:
        print(f"Descrição: {produto['nome']}")
        print(f"ID: {produto['id']}")
        print(f"Quantidade: {produto['quantidade']}")

while True:
    print("="*3, "CONTROLE DE ESTOQUE", "="*3)
    print("\n1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Sair\n")
    print("="*28)
    acao = input("Escolha uma opção: ")

    if acao == "1":
        cadastrar_produtos()
    elif acao == "2":
        listar_produtos()
    elif acao == "3":
        print("Encerrando o programa...")
        print("Salvando os produtos")
        time.sleep(5)
        break
    else:
        print("Opção inválida.")
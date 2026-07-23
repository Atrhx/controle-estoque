import time

produtos_estoque = []

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
            if codigo_existe == True:
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
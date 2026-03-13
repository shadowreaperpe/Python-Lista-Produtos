Lista = ["Nada", "Nada", "Nada", "Nada", "Nada", "Nada", "Nada", "Nada"]

while True:
    print("Lista Atual: ", Lista)
    p = input("Digite Um Produto: ")
    po = int(input("Qual Posição Deseja Colocar o Produto(0 A 7): "))
    Lista[po] = p
    sair = input("Deseja Adicionar Outro Produto? [S/N]").upper()

    if sair == "N":
        break
    else:
        continue
print("Lista Final: ", Lista)

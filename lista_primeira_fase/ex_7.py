codigos = []
compra = {}

for cod in range(0, 999):
    codigos.append(cod)

progama = True

while progama :
    proximo_id = codigos.pop(0)
    id = proximo_id
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    qtde = int(input("Digite a quantidade de produtos: "))
    compra.update()
    
    continua = str(input("Deseja continuar?: (Se sim digite 's' se não digite 'n')"))
    if continua == 's':
        continue
    else:
        progama = False
    
#Inicia a variavel "numero" que sera atualizada pelo usuario através do input posteriormente
numero = 0

#Inicia a variavel "total" que sera utilizada para somar os numeros recebidos pelo usuario

total = 0

while (numero != -1):
    numero = float(input("Digite um numero positivo ou -1 para encerrar o progama!: "))
    if numero > 0:
        total += numero
    else:
        print("Digite um numero positivo!")

print(total)

#-------------------------------------------------------------------------------------------------





    
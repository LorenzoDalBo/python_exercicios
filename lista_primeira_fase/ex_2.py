#Inicializa uma lista vazia onde serão adicionados os numeros passados pelo usuario
lista_numeros = [] 

for num in range(0, 10):  #Aqui eu passo o range de 0 a 10 para que o for itere 10 vezes no total, o mesmo resultado poderia ser conseguido com 1 a 11
    lista_numero = int(input("Digite um numero: "))
    lista_numeros.append(lista_numero) #Adiciona o numero passado para o usario a lista

print(lista_numeros)

lista_numeros.reverse() #O metodo "reverse" não retorna uma nova lista, apenas reverte a lista que ja existe

for numero in lista_numeros:
    print(numero)
    
lista = []

for num in range(0, 100):
    lista.append(num)
    
for numero in lista:
    if numero % 2 == 0:
        lista.remove(numero)
        
print(lista)
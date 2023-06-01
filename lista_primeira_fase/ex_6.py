import random

notas_turma_1 = []
notas_turma_2 = []
contador_turma_1 = 0
contador_turma_2 = 0

num_notas_turma = int(input("Digite quantas notas a turma tem: "))

for nota in range(1, num_notas_turma):
    nota_turma_1 = random.randint(1, 10)
    nota_turma_2 = random.randint(1, 10)
    notas_turma_1.append(nota_turma_1)
    notas_turma_2.append(nota_turma_2)
    contador_turma_1 += nota_turma_1
    contador_turma_2 += nota_turma_2

media_turma_1 = contador_turma_1/ num_notas_turma
media_turma_2 = contador_turma_2/ num_notas_turma

print(f"Notas turma 1: {notas_turma_1} \nMédia turma 1: {media_turma_1}\nNotas turma 2: {notas_turma_2}\nMedia turma 2: {media_turma_2}")


    


    
    


    


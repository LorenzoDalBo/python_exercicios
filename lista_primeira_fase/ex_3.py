medias_alunos = []

for aluno in range(1, 2):
    media = 0
    for nota in range(1, 5):
        nota_aluno = float(input("Digite a nota3 {} do aluno {}: ".format(nota, aluno)))
        media += nota_aluno 
    media = media/4
    medias_alunos.append(media)

alunos_aprovados = 0

for media_aluno in medias_alunos:
    if media_aluno >= 7 :
        alunos_aprovados += 1
        
print(alunos_aprovados)

    
        
        
    
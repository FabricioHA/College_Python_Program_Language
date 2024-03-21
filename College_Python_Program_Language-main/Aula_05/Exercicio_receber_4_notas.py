#Exercicio
#Receber 4 notas para cada aluno

notas = []

for indice in range(4):
    print(indice+1, " nota")
    nota = float(input())
    notas.append(nota)

media = nota/4

if media >=0 and media < 7:
    print(f"REPROVADO!!! NOTA {media}? por favor...")
elif media >=7 and media <= 10:
    print(f"APROVADISSIOMO RAPAZ!!! TIROU {media}! TÁ DE PARABÉNS")
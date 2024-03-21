"""
Tipo de dados:

string
int
decimal

O python não se preocupa om o armazenamento de valores de diferentes tipos na variavel,
pois python é uma linguagem fracamente tipada, pois não se preocupa com o armazenameto das variaveis entre os tipos,
por exemplo:

frutas = "maça"
frutas = "abacaxi"
frutas = 200

ele irá simplesmente substituir os valores dentro das variavel sem se preocupar com seu tipo, onde sua identificação
será a mesma
"""

frutas = "maça"
frutas = "abacaxi"
frutas = 200

print(frutas)

"""
O python criou variaveis chamadas de tipos extendidos onde, como o próprio nome sugere, são extensões 
dos próprios tipos pimitivos de dados como string, int, char e float, por exemplo.

Um exemplo claro disso é o que chamamos de vetores/matrizes, onde temos dois tipos de vetores:

Matrizes/vetores monodimensionais (referente a 1 coluna e várias linhas):

          Col. 1
Linha 0 |   0   |
Linha 1 |   1   |
Linha 2 |   2   |
Linha 3 |   3   |
Linha 4 |   4   |
Linha 5 |   5   |

outro tipo são as matrizes/vetores bidimensionais (2 colunas e varias linhas)

          Col. 1  Col. 2 
Linha 0 |   0   |   0   |
Linha 1 |   1   |   1   |
Linha 2 |   2   |   2   |
Linha 3 |   3   |   3   |
Linha 4 |   4   |   4   |
Linha 5 |   5   |   5   |

Lembrando que o vetor sempre começa com o indice 0, ou seja, temos 6 linhas com indices de 0 a 5.

O armazenamento do indices pode ser qualquer tipo de dados, ou seja, em uma linha temos um int, outra float e
em outra string. por exemplo:

Variavel: Frutas
indice | Conteudo       |
0      | "Maça"         |
1      | 10000          |
2      | "Bananão"      |
3      | 56.7           |
"""

frutas = ["Ricardão", "Maçã", "Bananão", "Mandiocão", "Ai que perão"]

print(frutas[0])
print(frutas[4])

"""
Podemos classificar a lista de vetores em ordem alfabética, organizada, e para tal podemos aplicar o método sort()
"""
frutas.sort() #Nota: Esse método não funciona ao tentar concatenar valores de texto com valores numéricos
print(frutas) #Irá exibir os indices em ordem alfabética

"""
Para incluirmos mais de uma linha/indices/index, utilizamos o método append(), onde permite a inclusão de um valor por
vez a cada declaração:
"""

frutas.append("Amora") # Ele irá incluir o valor depois do ultimo indice
print(frutas)
#Resultado: ['Ai que perão', 'Bananão', 'Mandiocão', 'Maçã', 'Ricardão', 'amora']

"""
Perceba que acima, amora não ficou organizada em ordem alfabética. Isso acontece pois a execução do sort não é 
constante, pois é como se ele reorganiza-se os indices dentro das variaveis de acordo com sua ordem alfabética, e só
irá organizar esse valor se declaramos o metodo sort novamente:
"""

frutas.sort()
print(frutas)
#Resultado: ['Ai que perão', 'Amora', 'Amora', 'Bananão', 'Mandiocão', 'Maçã', 'Ricardão']

"""
Agora iremos utilizar os métodos de loop, sendo o primerio for:

Nesse caso acima, a estrutura é algo como:

para indices em vetor faça...
    imprimir conteudo dos indices

Perceba que criamos uma "variavel dentro do for para representar a variavel frutas e imprimir seus indices do 
0 ao 5 (6 index no total)
"""

for fruta in frutas: 
    print("Fruta -> " + fruta)

#Vamos agora conhecer uma formatação de texto chamado f string

"""
Sua sintaxe seria algo como:

f"texto {variavel} texto"

Vamos utilizar o loop acima de exemplo do exercicio de nota para exibir o resultado em uma linha no input:
"""

notas = []

for indice in range(4):
    nota = float(input(f"Digite a {indice+1} nota: "))
    notas.append(nota)

print(notas)

"""
Basicamente, o f string é capaz de concatenar variaveis ou númeos com texto para imprimir valores 
facilmente. O método de impressão do C também deve funcionar. Vamos testar: 
"""

notas = []

for indice in range(4):
    nota = float(input("Digite a %d nota: " %(indice+1)))
    notas.append(nota)

print(notas)
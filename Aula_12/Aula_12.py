"""
===    Machine learning    ===

Inteligencia artificial (IA ou AI) é basicamente como uma emulação da forma como o ser humano pensa mesclado com a forma
como os dados são processados em um computador.

Para tal, criamos o que chamamos de rede neural, capaz de criar neuronios artificiais para um computador ser
capaz de executar e aprender como nós.

Os passos para criar uma rede neural seria algo como:

1 criar um "cerebro" artificial vazio.
2 Mapear pontos de sinápses que ele irá utilizar para armazenar dados e informações que ele irá interpretar 
para retornar informações a partir dessa coleta de dados

O Machine Learning nesse contexto nada mais é do que um framework dentro da IA.

As bibliotecas referente a IA seriam:

- Biblioteca de tratamento de imagem
    - Pillow
    - OpenCV Python
    - Luminoth
    - Mahotas

- Bibliotecas para vizualização de dados
    - Matplotlib
    - Brokeh
    - Seaborn
    - Altair

- Biblioteca para tratamento de textos
    - Punctuation
    - NLTK
    - FlashText
    - TextBlob

- Internet, rede e cloud
    - Requests
    - BeautfulSoup
    - s3fs

- Bibliotecas para acesso a banco de dados
    - mysql-connector-python
    - cx-oracle
    - psycopg2
    - SQLAlchemy

##########################################
###- Deep Learning - Machine Learning
###    - Keras
###    - TensorFlow
###    - PyTorch
###    - Scikit Learn
##########################################

- Biblioteca para jogos - PyGame
    - PyGame


Afinal, o que é Machine Learning?
É basicamente um processo de auto aprendizado, sem isso 
ser explicitamente programado, possibilando que o ML faça o 
sistema aprender com dados, identifiquem padrões e façam
previsões.

Podemos aplicar esse cara em:

-Reconhecimento de imagens: Identificar objetos, rostos e até
mesmo emoções em fotos e videos

-Processamento de linguagem natural: entender e gerar lingua 
humana.

-Previsão de séries temporais: Prescrever eventos futuros

-Análise de sentimentos: Extrair opiniões e sentimentos 
de textos e mídias sociais

===============================================================
Temos 4 tipos de machine learning a ser aplicado na IA, sendo
eles:

1. Aprendizado supervisionado: Ele recebe exemplos especificos
e rotuládos, como imagens e vídeos, identificando uma 
probalidade a partir desse banco de dado já pré treinado

2. Aprendizado não supervisionado: Esse é feito a partir de
tentativa e erro, onde caso verdadeiro o sistema é recompensado,
caso falso é penalizado

3. Aprendizado Semi-Supervisionado: Você recebe alguns rótulos
e dados não rotulados forçando-o a aprender com os dados 
rotulados recebidos e decifrar por conta a partir da informação
disponivel os dados pouco ou não rotulados.

4. Aprendizado por reforço: Semelheante ao método não 
supervisionado, mas nesse caso ele realmente não tem dados
pré estabelecidos ou de base para resolver os rótulos,
tendo assim que decifrar por tentativa e erro puro.

===============================================================
KNN: Desvendado os segredos do algoritimo dos vizinhos mais
próximos!

O KNN  é uma ferramenta que toma decisões a partir de 
informações dos vizinhos mais próximos no conceito e machine
learning.

Ele é um algoritmo de aprendizado supervisionado, precisando 
de exemplos já rotulados:

    1 Defina o k
    2 Calcule as distâncias
    3 Identifique os vizinhs
    4 Faça a previsão
==============================================================
Vantagens do KNN
- Simplicidade: É um algoritimo fácil de entender
- Versatilidade: Ele pode ser usado para problemas de 
classificação quanto de regressão
- Eficiência: O KNN é eficiente para conjuntos de dados de 
tamanho médio

Desvantagens do KNN
- Dimensão da Maldição: O desempenho pode ser afetado por 
conjuntos de dados com alta dimensionalidade
- Sensibilidade ao Ruído: O KNN pode ser sensível a outliers 
(pontos fora da curva) nos dados.
- Escolha do K: A escolha do valor ideal para k pode ser crucial
para o bom desempenho do algoritimo
==============================================================
DataSet Iris: Utilizado como base para aprendizagem em 
machine Learning

O dataset Iris tem três espécies de flores: Iris setosa, iris
virginica e iris versicular. Ele possuiu 150 amostras, sendo 50
amostras para cada espécie:

    -Comprimento da Sepala (cm): Comprimento da parte externa da
    pétala
    -Largura da sepala (cm): Comprimento da parte interna da 
    pétala
    - Largura da pétala (cm): Largura da parte interna da 
    pétala

Vamos começar a usar a biblioteca scikit-learn. Para tal,
vamos instalar o pelo comando pip install scikit-learn 
"""

#Importando dataset inicio
from sklearn.datasets import load_iris
iris = load_iris()

print(iris.data)
#Importando dataset fim

print("\n")

#Resultados valores de pesquisa targets Inicio
print(iris.target_names)
print(iris.target)
#Resultados valores de pesquisa targets fim

print("\n")

#Inicio X e Y (Separando os dados e resultados)
x = iris.data
print(x)

print("\n")

y = iris.target
print(y)

print("\n")
#Fim X e Y (Separando os dados e resultados)


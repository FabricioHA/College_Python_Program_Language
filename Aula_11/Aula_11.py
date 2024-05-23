"""
#Biblioteca "Pandas"#


Pandas: Painel de dados
    L Bibliotecas: Seriam referentes a pacotes/modulos separados que podem ser acoplados dentro das sua funções padrões.
    L Insights: São momentos de compreensão subita ou intuitiva sobre algo, como quando idéias inovadoras que podem 
    surgir a partir de Insigths, muito comun esse tipo de aplicação de ideias na área de TI

O que seriam dados como um todo? Podemos atribuir a dados algo como texto, números, gráficos, fotos, filmes, livros, etc.


Pandas é uma biblioteca para ciencia de dados e Open Source voltada  para python, propondo uma abordagem rapda e flexivel
com estruturas robustas para se trabalhar com dados relacionais(ou rotulados).
Temos dois objetos/classes importantes: 
    Series e DataFrames

Series: Seria básicamente uma lista unidimensional 
NOME = |"fAB"|
       |"jAO"|     
       |"wIL"|
       |"vTI"|
       |"DEV"|
        
    ...

Dataframe: Semelheante ao series, mas é capaz de gerar várias colunas e linhas com indices gerados automaticamente,
uma estrutura muito semelheante a banco de  dados, tornando-o uma espécie de array bidimensional
INDEX   NOME    IDADE   ALTURA
0       "fAB"   12      1.76
1       "jAO"   32      1.43
2       "wIL"   32      1.23
3       "vTI"   76      1.09
4       "DEV"   98      1.99
    ...
Ou seja, Dataframe nada mais é do que uma junção de várias series dentro de um unico dataframe, como mostrado acima

Vamos colocar a biblioteca em prática
"""
import pandas as pd #Este "as pd" nada mais é do que um encurtador/apelido ao referenciarmos pandas ao longo do código

# Criando um DataFrame
dados = {"nome": ["Alice", "bob", "Charlie", "Douglas", "Carol"],
         "idade": [25, 90, 76, 15, 60],
         "cidade": ["Nova Yoirk", "Los Angeles", "São Paulo", "Santos", "Santos"]}

print("\n")
print(dados)

df = pd.DataFrame(dados) #Apartir do pandas, iremos importar a classe/objeto DataFrame e converter a lista acima em um dataframa

# Como se ele puxasse um select * no banco, exibindo toda a tabela/dataframe 
print("\n")
print(df)

# Agora, uma pesquisa especifica exibindo apenas uma coluna:
print("\n")
print(df.nome)

#Verificar a versão instalada do pandas
print("\n")
print(pd.__version__)

#Nos mostra o tipo de dados de cada coluna 
print("\n")
print(df.dtypes)

# Ele exibe um resumo das caracteristicas tipos, tamanho alocado e quantidade decampos prenchidos do dataframe
print("\n")
print(df.info())

#Pesquisa um campo específico do indice especificado no iloc
print("\n")
print(df.iloc[1])

#Retorna valores bool referente a quais linhas tem idade maior que 25, se verdadeiro, true, se falso, false
print("\n")
print(df.idade > 25)

#Ele vai somar todas as idades usando cidade como parametro para condição de soma
print("\n")
print(df.groupby("cidade")["idade"].sum())

filmes = pd.read_csv("./contents/movie.csv")

print(filmes.info())
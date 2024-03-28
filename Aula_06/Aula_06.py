"""
API's

Aplication Program Interface (Interface de Programação de Aplicação). Refere-se a um site com função distinta.
Ela funciona como um contrato que requisita um conjunto de regras para manipular algum elemento dentro da linguagem
de programação.

Simplificando, ela dita regras e padrões para manipularem elementos

"Uma API é um garçom que traz a sua comida, e o REST é um tipo de comanda. 
Quando o garçom usa a comanda REST, ele é um garçom RESTFUL"
"""

"""
Dicionário - Tipo de dados - python

São coleções desordenadas de items
Equanto outras coleções, como listas, são indexadas por uma faixa de números, os dicionários são indexados por chaves,
que podem ser qualquer tipo imutavel (constantes).
Cada par chave-valor em um dicionário é separado por virgulas e todo conjunto é colocado entre chaves {}:

dicionário|  chave | valor |  chave | valor
meu_dict = {"nome": "Alice", "idade":  25}

nomeDoDicionario = {"chave": "valor", "chave2": "valor2"}

"""


#Para declarar um dicionário de dados no python, fazemos:
dicionarioVazio = {}

#Um dicionário com dados seria:
dicionarioPreenchido = {"nome": "Fabrício", "idade": 21}
print(dicionarioPreenchido) #Exibimos toda a extrura do dicionário
print(dicionarioPreenchido["nome"])#Exibimos apenas uma chave específica da chave

#Para acessar os valores de um dicionário via chave declaramos o nome do dicionario e usamos colchetes com a chave:
nome = dicionarioPreenchido["nome"]
print(nome)


"""
Método .get (buscar chaves)

Ele trabalha com uma busca no dicionário, especificando qual a chave, caso não encontre, ele tem um parametro
que faz um tratamento de erro exibindo uma mensagem caso a chave não seja encontrada:
"""
profissao = dicionarioPreenchido.get("profissao", "Não encontrado")
print(profissao)
#Resultado: Não encontrado

nome = dicionarioPreenchido.get("nome", "Não encontrado")
print(nome)
#Resultado: Fabrício

"""
Adicionar uma nova chave:

Podemos adicionar ou modificar uma nova chave especifiando em colchetes seu nome e atribuir seu valor:
"""
dicionarioPreenchido["profissao"] = "Pistoleito"
print(dicionarioPreenchido["profissao"])
print(dicionarioPreenchido)

"""
Método .pop e del (Remover elementos de um dicionario)

Podemos remover um elemeto específico através do método por simplesmente declarar a chave no parametro no método pop:

nomeDoDicionario.pop("nomeDaChave")

para deletar um dicionário inteiro, utilizamos o método del

"""
dicionarioPreenchido.pop("profissao")
print(dicionarioPreenchido.get("profissao", "Não especificado"))

"""
para deletar um dicionário inteiro, utilizamos o del:
"""
del dicionarioPreenchido


"""
Metodos keys() e values() e items()
"""

#para mostrar apenas chaves:
dicionarioPreenchido = {"nome": "zé", "idade": "infinita"}
print(dicionarioPreenchido.keys())

#para mostrar valores:
print(dicionarioPreenchido.values())

"""
Interação em dicionários: é como se ele separa-se os objetos dentro dicionário, possibilitando a utilização de loops
para imprimir um por um
"""
for chave, valor in dicionarioPreenchido.items():
    print(f"{chave}:{valor}")

"""
Aninhamento

Podemos criar dicionários dentro de dicionários, possibilitando a criação de "tabelas" dentro dos dicionários,
encapsulando-os:
"""
familia = {
    "pai": {"nome": "João", "idade": 54},
    "mãe": {"nome": "Maria", "idade": 40}
}
print(familia.keys()) #Imprime as chaves do dicionário familia
print(familia["pai"]["idade"]) #Imprime a idade de pai, como se eu seleciona-se a linha pai e a coluna idade do pai
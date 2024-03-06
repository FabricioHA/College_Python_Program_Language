"""
Nesta aula, iremos trabalhar com caracteres alfanuméricos, chamados 
de strings. as strings nada mais são do que um conjunto de chars 
(caracteres) separados por indices.

===Lembrando que em python, string é considerado um objeto, 
tendo duas caracteristicas, com atributos e métodos.===

-Nota: métodos são funções dentro da linguagem python.

Veja o exemplo abaixo:
"""

nome = "fabrício"

"""
Nesse caso acima, criamos uma variável "nome", o seu tipo será
definido pelo valor que ela é atribuida. Em termos ilustrtivos,
imagine que temos um armário (memória) onde pegamos uma gaveta
que armazena um tipo de dado. Para puxar esse dado em especifico
no armário, rotulamos a gaveta com um rótulo, uma identificação 
para essa variavel.

Para consultarmos o tipo de valor que a variável contém, utilizamos
a função type(), como nos exemplo abaixo:
"""

print(type(nome))
#Resultado: <class 'str'>

ano = 2024
print(type(ano))
#Resultado: <class 'int'>

ano = 2024.1
print(type(ano))
#Resultado: <class 'float'>

"""
A variável nada mais é do que um rótulo para facilitar sua 
localização na memória, mas ele ainda tem uma identificação
própria na memória, sendo ela:
"""

print(id(nome))
#Resultado: 138649260486320 

"""
Esse valor acima é referente a posição da variável na memória
"""

"""
Com o conceito de indices e objetos, podemos utilizar métodos
para, por exemplo, utiliar um ToUpperCase nos caracteres,
como por exemplo: 
"""

print(nome.upper())
#Resultado: FABRÍCIO

print(nome.lower())

"""
Nota: os parenteses nesses métodos são chamados de paramentros
pois eles são valores que irão determinar os parametros necessários
para executar uma função, dependendo das suas regras

Temos dois tipos de variáveis, sendo eles multaveis e imultaveis:

ou seja, quando seu conteudo muda, seu endereço de memória muda,
como quando trocamos ou alocamos o conteudo de uma gaveta para outro
espaço.
"""

print(id(nome))
#Resultado: 138648476536720

"""
Perceba que o valor acima mudou, então isso indica que a variável
é do tipo mutavel
"""

"""
Também podemos utilizar um método/função chamado de replace(),
capaz de subistiuir caracteres dentro de uma string, definindo
o caractere que iremos mudar e o caracteres que iremos substituir
no lugar (nos dois casos são parametros)
"""

print(nome.replace('f','p'))
#Resultado: pabrício

"""
Podemos também concatenar as funções e métodos para misturar
suas funções:
"""

print(nome.replace('f','p').replace('b', 't').upper())
#Resultado: PATRÍCIO

"""
outro método muito interessante também o método count(), capaz de
contar quanto caracteres que definimos dentro do seu parametro
existem:
"""
produto = "banana"
print(produto.count('a'))
#Resultado: 2

"""
Nesse ponto, iremos trabalhar com fatiamento de strings,
utilizando o conceito de vetores e matrizes, onde cada posição
de um caracteres na string é um indice sequencial começando  sempre
da posição "0":
"""

print(produto[0:2])
#resultado: ba

"""
Mas por que o caracteres não foi impresso de acordo com a posição 
final definida? 
Simples, é como se houvesse uma operação lógica padrão de

0 < 2 == [0:2]

ou seja, caso o indice final definido seja menor que 2, ele irá
exibir tudo aquilo menor que dois
"""

"""
Agora, iremos trabalhar com operadores lógicos, sendo eles:
< menor
> maior
== igual
>= maior ou igual
<= menor ou igual
!= diferente

eles são os comparadores entre valores para determinar se uma valor
tal operação é verdadeira ou falsa (true/false)
"""

print(5>6)
#Resultado: False
print(5<6)
#Resultado: True
print(5==6)
#Resultado: False
print(5>=6)
#Resultado: false
print(5<=6)
#Resultado: true
print(5!=6)
#Resultado: true

"""
Outros operadores lógicos de comparação são chamados de || (or)
e and (&&).

Por exemplo em AND, uma operação só será 
verdadeira se uma E(AND) outra for verdadeira. Caso uma das duas
seja falsa, ela será anulada.

No outro caso OR, se um valor ou (OR) outro for verdadeiro, caso
um dos valores seja verdadeiro, a operação será verdadeira.

"""
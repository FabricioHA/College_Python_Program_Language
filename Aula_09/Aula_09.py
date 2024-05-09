"""
Programação Orientada a Objeto Parte 2

Histório do paradigima: Orientação a Objetos

O criador do POO foi Alan Kay, que também criou o SmallTalk.
A idéia de POO ganhou impulso em 1970 com C++ e Java.

Paradigma siginifica modelo, padrão, onde no contexo da 
programação, um paradigima é um jeito, uma maneira, um estilo de 
se programar.
"""

"""
Abaixo mostramos uma sintaxe para instanciar objetos:
"""

from re import T


class nome_classe:
    def __init__(self,variavelA=0,variavelB=0): #o self seria eu, ele mesmo, no gearal
        self.varA = variavelA
        self.varB = variavelB

"""
nesse contexto, é como se ele mesmo atribuisse as suas 
caracteristicas dentro dele mesmo, ou melhor,
"inside myself"...

def modulo(self) >> Criação de uma função com métodos
self.varA >> utiliza uma variável "recebida" pela classe (objeto)

Vamos definir uma classe com seus atributos e métodos: 
"""


class TV: #definir classe
    def __init__(self, tam=49, mc="LG"): #Definir atributos
        self.marca = mc
        self.modelo = "54h33"
        self.cor = 'preto'
        self.tamanho = tam
        self.canal = "netflix"
    
    #Definir métodos/funções
    def muda_canal(self, novo_canal=""): 
        if novo_canal == "":
            pass
        else:
            self.canal = novo_canal

#objetos
tv_sala = TV(90, "Samsung")
tv_quarto = TV() #Se vazio, ele pega o valor atribuido nos parametros

tv_sala.muda_canal()

print("A marca da tv na sala é %s, e está no canal %s..." %(tv_sala.marca, tv_sala.canal))
print("O tamanho da tv no quarto é de %d'' polegadas" %(tv_quarto.tamanho))
"""
def nomeDaFuncao(parametros):
    return operação/resultado

Acima, temos uma estrutura básica de uma função. 

Normalmente, para invocarmos uma função, podemos fazer da seguinte maneira:

nomeDaFuncao(parametros)

Procuraremos também criar defaults na variavel, caso o usuário não digite os valores requisitados:

minhafuncao(var1 = 0, var2 = "muchas gracias")

Podemos executar essas estruturas na prática, como listado abaixo:
"""

#Inicio Funções
def validarValor(value):
    while True:
        if not value.isnumeric():
            print("Errado, Digite o valor novamente.")
            return True
        else:
            value = float(value)
            break
    return value

def calculadora(opt=1, n1=0, n2=0):
    if opt == 1:
        return n1 + n2
    
    elif opt == 2:
        if n2 > n1:
            return n2 - n1
        elif n1 > n2:
            return n1 - n2
    
    elif opt == 3:
        return n1 / n2 
    
    elif opt == 4:
        return n1 * n2
    
    else:
        return "Opção selecionada incorretamente"
#Fim Funções

#Inicio Entrada de dados
valor1 = input("digite o primeiro valor: ")
validarValor(valor1)

valor2 = input("digite o segundo valor: ")
validarValor(valor2)

opcao = int(input("digite a operação deseja:\n\n 1 para Soma   2 para Subtração  3 para Divisão  4 para multiplicação\n\nDigite sua opção: "))
#Fim Entrada de dados

#Inicio Saida de dados
print(calculadora(opcao, float(valor1), float(valor2)))
#Fim Saida de dados
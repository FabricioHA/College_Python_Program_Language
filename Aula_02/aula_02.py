"""
No exemplo abaixo, criamos uma variavel com nomes para serem alocados em algum espaço na memória
Uma variavel não pode ter nome maiusculo no inicio da variável
"""
salario = 1000 #maneira correta de declaração de variáveil 
Salario = 2000 #maneira incorreta de declaração de variável

#instruções no python sempre são em caracteres minúsculos
print(salario) #Comandos builtin_function_or_method são comandos/objetos nas quais o python já sabe o que fazer

del Salario 
"""
O comando/objeto del é para eliminar uma variável e seu valor da memória do computador. se você tentar chamar a variavel "Salario" novamente
o python irá emitir um erro afirmando que o nome da variável não foi definido, pois seu valor já não está mais na memória. 
"""

"""
Calculo de aumento de salário. Nesse caso, o 1.5 é referente a 150%, ou seja, 100% do salário original + 50% do mesmo salário
"""
print(salario*1.5) #Podemos fazer operações matematicas dentro do print, mas normalmente a forma correta seria:

salario = salario * 1.5

print(salario)
"""
Nesse caso, ele pega o valor original da variavel salário, e multiplica por um numero que representa a porcentagem do mesmo, sendo apenas 
necessário printar a variavel com o valor armazenado, não a variável em sí.
"""

print("Boa noite")#A maioria dos comandos possuem parametros, normalmente declarados entre parenteses, o boa noite é o parametro que o print irá executar em cima

print("Seu salário é R$",salario) #Virgula é capaz de concatenar variáveis e ainda criar um index de espaço entre o texto e a variaval ou dado a ser impresso

salario = input("Digite seu salário: R$") #input() é entrada de dados. Para entrar com um valor, digite o que é requisitado pelo programa e depois tecle enter
print("Seu salário é igual a R$",salario)
#Exemplos Aula_01 Linguagem de programação

print("\n\nSeletor de código python Aula 01\n\n1 - Hello Wolrd program  2 - Loop Code   3 - Multiplicador\n\n")

code_opition = input("Digite A opção desejada: ")
int(code_opition)

if code_opition == "1":
    b = 10
    a = "hello world my " + str(b) + " students" #Não tem como concatenar valores numéricos e strings em python, então precismamos
                                             #converter a varivael de valor inteiro em string antes de exibir em uma concatenaçãos
    print(a) #Impressão em algo em algo equivalente a "console" no javascript ou C

elif code_opition == "2":
    #Loop for no Python
    i = 0
    for i in range(1, 7):
        print(i)

elif code_opition == "3":
    Multiplicador1 = 10 * 3 #Operação demultiplicação
    multiplicador2 = 10 ** 3 #Operação de multiplicação potencialiadora
    print(Multiplicador1, multiplicador2)
else:
    print("Valor inválido... Imbecil :)")
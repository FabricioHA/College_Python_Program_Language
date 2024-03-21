#calculo do IMC
#imc = peso / altura * altura

#Inicio entrada de dados
while True:

    peso = input("Digite seu peso atual: ")
    altura = input("Digite sua altura atual: ")

    if not peso.replace(".", '').isnumeric() or not peso.replace(".", '').isnumeric():
        print("Valores inválidos, digite novamente.")
    else:
        peso = float(peso)
        altura = float(altura)
        break
#fim entrada de dados

#processamento
imc = peso/(altura*altura)

#Inicio saida de dados (começamos a ver as faixas condicionais)
print("\nSeu IMC é %.2fKg/m2" %(imc))
if imc <= 18.5:
    print("\nVocê está abaixo do peso\n")

elif imc > 18.5 and imc <= 24.9:
    print("\nPeso ideal (Parabéns)\n")

elif imc > 25.0 and imc <= 29.9:
    print("\nLevemente acima do peso\n")

elif imc > 30.0 and imc <= 34.9:
    print("\nObesidade Grau I\n")

elif imc > 35.0 and imc <= 39.9:
    print("\nObesidade Grau II (Severa)\n")

elif imc >= 40:
    print("\nObesidade III (Mórbida)\n")
#fim saida de dados
from optparse import Option

print("=====Impressão de meses usando If/Else=====")
print("Digite os os três primeiros caracteres de um mês.\n\nMas antes disso...\n")

while True:

    opition = input("Deseja executar o sistema?[y/n]")

    if opition == "y": 

        month = input("\nDigite os três primeiros caracteres de um mês: ").upper()

        if month == 'JAN':
            print("\nJaneiro\n")

        elif month == "FEV":
            print("\nFevereiro\n")

        elif month == "MAR":
            print("\nMarço\n")

        elif month == "ABR":
            print("\nAbril\n")

        elif month == "MAI":
            print("\nMaio\n")

        elif month == "JUN":
            print("\nJunho\n")

        elif month == "JUL":
            print("\nJulho\n")

        elif month == "AGO":
            print("\nAgosto\n")

        elif month == "SET":
            print("\nSetembro\n")

        elif month == "OUT":
            print("\nOutubro\n")

        elif month == "NOV":
            print("\nNovembro\n")

        elif month == "DEZ":
            print("\nDezembro\n")
        else:
            print("\nValor digitado incorretamente\nDigite novamente.")
    elif opition == "n":
        print("Programa finalizado...")
        break
    else:
        print("\nValor digitado incorretemante\n")
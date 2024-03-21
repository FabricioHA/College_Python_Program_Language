#Calculo do IRRF
salarioBruto = input("Digite seu salário atual: ")
salarioBruto = float(salarioBruto)

if salarioBruto <= 2112:
    aliquota = 0
    deducao = 0
    print("Salário bruto de R$%.2f"%(salarioBruto))
    
elif salarioBruto > 2112 and salarioBruto <= 2826.65:
    aliquota = 0.075
    deducao = 150.40 

elif salarioBruto > 2826.66 and salarioBruto <= 3751.05:
    aliquota = 0.15
    deducao = 370.40 

elif salarioBruto > 3751.06 and salarioBruto <= 4664.68:
    aliquota = 0.225
    deducao = 651.73 

elif salarioBruto > 4664.68:
    aliquota = 0.275
    deducao = 884.96 

if aliquota != 0 and deducao != 0:
    aliquota = salarioBruto*aliquota
    deducao = aliquota - deducao
    salarioLiquido = salarioBruto - deducao

    print("Salario bruto: R$%.2f  Alicota: R$%.2f  Dedução: R$%.2f  Salário liquido: R$%.2f" %(salarioBruto,aliquota,deducao,salarioLiquido))
#Calculo do IRRF
salarioBruto = input("Digite seu salário atual: ")
salarioBruto = float(salarioBruto)

if salarioBruto <= 2112:
    print("Apenas Salário bruto de R$%.2f"%(salarioBruto))
elif salarioBruto > 2112 and salarioBruto <= 2826.65:
    aliquota = salarioBruto*0.075
    deducao = aliquota - 158.40
    salarioLiquido = salarioBruto - deducao

elif salarioBruto > 2826.66 and salarioBruto <= 3751.05:
    aliquota = salarioBruto*0.15
    deducao = aliquota - 370.40 
    salarioLiquido = salarioBruto - deducao

elif salarioBruto > 3751.06 and salarioBruto <= 4664.68:
    aliquota = salarioBruto*0.225
    deducao = aliquota - 651.73 
    salarioLiquido = salarioBruto - deducao

elif salarioBruto > 4664.68:
    aliquota = salarioBruto*0.275
    deducao = aliquota - 884.96 
    salarioLiquido = salarioBruto - deducao

print("Salario bruto: %f  IRRF: %f ")
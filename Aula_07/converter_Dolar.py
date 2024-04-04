#Cotação moedas - Dolar
import requests
import json

"""
#From datetime import datetime
"""
#Quantidade de dias
#dias = int(input("informe a quantidade de dias"))

requisicao = requests.get("https://economia.awesomeapi.com.br/json/all/USD-BRL")
#requisicao = requests.get("https://economia.awesomeapi.com.br/json/all/USD-BRL")

cotacao = requisicao.json()

print("### Cotação do Dolar ###")
print("Moeda" + cotacao['USD']['name'])
print("Data" + cotacao['USD']['create_date'])
print("Valor Atual: R$" + cotacao['USD']['bid'])
# https://viacep.com.br/ws/09664000/json/

import requests #Permite ao python requisitar recursos externos na internet, por exemplo
import warnings #Bibliotecas referentes a mensagens de erros
warnings.filterwarnings("ignore")

cep = input("Informe o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

ret = requests.get(url, verify = False).json()

dados = ret
print("_"*80)

print(f"Rua {dados['logradouro']}")
print(f"Bairro {dados['bairro']}")
print(f"Estado {dados['uf']}")
print(f"IBGE {dados['ibge']}")
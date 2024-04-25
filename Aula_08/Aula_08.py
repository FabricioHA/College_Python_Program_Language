"""
Programação Orientada a objeto (POO)

===========================================
Objetos: Todo objeto tem uma caracteristica, uma "PROPRIEDADE".;

Ou seja, eu posso criar um objeto, uma classe, uma estrutura, com
todas as suas caracteristicas.

essa classe ainda não é um objeto, mas tem suas caracteristicas.

Para que possamos criar um objeto, "INSTANCIAMOS" esse objeto (classe)
que será utilizada para determinada função ou propriedade no
sistema.
===========================================
"""

"""
-Função (function)
    seria um bloco de código que podemos reutilizar várias vezes
    de acordo com seu parametros.

    Estático (static) ou dinâmico (dynamic)
        Estático: Não pode ser reutilizado
        dinamico: Pode ser reutilizado várias vezes
        ao ser chamado.
            Sua estrutura se baseia em parametros de valores
            para ter um ponto de partida e um retorno de valor
            baseado nos parametros informados.
"""
#Exemplo de função:
def mensagem():
    print("Boa noite... Danada!!!")

mensagem()

#Segundo exemplo:
def mensagem():
    texto = "Boa noite... Danada!!!" 
    return texto #Retorna o valor da variavel texto

print(mensagem())

#Utilizando parametro na função:
def mensagem(periodo, quem):
    texto = f"Boa {periodo}... Danada!!!{quem.upper()}"
    return texto

print(mensagem("tarde", "Rasputia"))

#Função com if else
def parImpar(v1):
    if v1 % 2 ==0:
        return "Par"
    else:
        return "impar"

print(parImpar(10))

"""
Vamos fazer uma função com vários parametros (*args, ou **kwargs)
para *args=lista
para **kwargs = dicionário

nota
"""

#*args
def muitosParametros(*args): #Nesse caso, iremos definir que podemos armazenar um valor várias vezes
    for parametro in args:
        print(f"Você passou o parametro: {parametro}")

muitosParametros(10, 20, 'Maria', 'Pedro') #Dessa forma, graças ao for iremos

#**kwargs
def muitosParametrosDicionario(**kwargs):
    print(kwargs.values())

muitosParametrosDicionario(nome = "Fabricio", idade = 56)


#função soma
def soma(n1, n2, n3):
    return n1 + n2 + n3

print(soma(90,1000,500))
"""
Nesse caso acima, se eu deixar de prencher um dos parametros, terei um erro, pois os mesmos
não foram preenchidos. Dessa forma, podemos atribuir um valor padrão para evitar tal erro, por exemplo "0"
"""
#função soma com tratamento de erro
def soma(n1=0, n2=0, n3=0):
    return n1 + n2 + n3

print(soma(90,1000,500))
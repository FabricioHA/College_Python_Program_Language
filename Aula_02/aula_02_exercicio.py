"""
Exercício

1 - Pedir um número de segundos
"""

totalSecond = input("Digite os os segundos necessários: ")
totalSecond = float(totalSecond)

day = totalSecond//86400
day = int(day)

hour = totalSecond // 3600
hour = int(hour)

min = (totalSecond%3600)//60
min = int(min)

sec = (totalSecond%3600)%60
sec = int(sec)

print("O tempo total é de "+str(day)+" dia(s), totalizando "+str(hour)+":"+str(min)+":"+str(sec))
"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

sequencia = [0]

n = int(input('Digite até onde deseja que a sequência vá: '))
num = int(input('Digite um número: '))

anterior = 0
proxima = 1
soma = 1

for n in range(anterior, n - 1):
    soma = proxima + anterior
    anterior = proxima 
    proxima = soma
    sequencia.append(anterior)


if num in sequencia:
    print(f'O valor {num} está na sequencia')

else:
    print(f'O valor {num} NÃO está na sequencia')

print(sequencia)
"""2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre."""

palavra = input('Digite uma palavra: ').lower()


if 'a' in palavra:
    print('A letra "a" está presente na string')
    qtd_vezes_a = palavra.count('a')
    print(f'e aparece {qtd_vezes_a}')

else:
    print('A letra "a" não aparece na string')
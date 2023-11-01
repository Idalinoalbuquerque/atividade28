# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


numero = []
for n in range (0,7):
    adn = int(input("digite o adn: "))
    if adn <=2005:
        print("maioridade")
    else:
        print("menor de idade")
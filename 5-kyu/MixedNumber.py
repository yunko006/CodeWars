"""
Examples :
Examples
Input: 42/9, expected result: 4 2/3.
Input: 6/3, expedted result: 2.
Input: 4/6, expected result: 2/3.
Input: 0/18891, expected result: 0.
Input: -10/7, expected result: -1 3/7.
Inputs 0/0 or 3/0 must raise a zero division error.
"""

from fractions import Fraction


def mixed_fraction(s):
    index = s.index('/')
    dividende = s[:index]  # nombre avant la fraction
    diviseur = s[index + 1:]  # nombre apres la fraction

    division = int(dividende) / int(diviseur)

    # permet de connaitre la partie entiere de la division
    entier = int(division)

    # abs pour etre sur que reste est positif, car c'est que l'entier qui doit etre positif ou négatif
    if entier:
        reste = abs(division - entier)
    else:
        reste = division
    fract = Fraction(str(reste)).limit_denominator(10000000)

    if dividende == "0":
        return "0"
    if entier == 0:
        return f"{fract}"
    if fract == 0:
        return str(entier)
    else:
        return f"{entier} {fract}"


# a = mixed_fraction('-4306982/8569312')
# print(a)

#!/bin/bash

import math

def adivinador(q, r, b, e):
    """
    q: Número Previo
    r: Resultado
        - El número a adivinar es menor que el proporcionado    -1
        - No se sabe si el número a adivinar es mayor o menor   0
        - El número a adivinar es mayor que el proporcionado    1
    b: Begin (Inicio) del Rango
    e: End (Fin) del Rango
    """
    if r==0:
        return q
    elif r == -1:
        e = q - 1
        q = math.floor((b + e) / 2)
        return adivinador(q, 0, b, e)
    elif r == 1:
        b = q + 1
        q = math.floor((b + e) / 2)
        return (q, 0, b, e)


def main():
    print("Indique el rango de números a adivinar")
    b = int(input("Limite Inferior: "))
    e = int(input("Limite Superior: "))

    q = math.floor((b + e) / 2)
    r = 0
    while r != 2:
        q = adivinador(q, r, b, e)
        print(f"Creo que es el {q}")
        print("Escribe:")
        print("\t-1\tSi tú número es menor")
        print("\t1\tSi tú número es mayor")
        print("\t2\tSi es el número correcto")
        r = int(input("? "))


if __name__ == "__main__":
    main()


"""
Cualquier cadena puede ser descompuesta en secuencias de palíndromos. Por ejemplo, la
cadena ARACALACANA se puede descomponer de las siguientes formas:
ARA CALAC ANA
ARA C ALA C ANA
A R A CALAC A N A
etc.
(en el peor de los casos, un texto de longitud n se dividirá en n cadenas de longitud 1)
Desarrollar un algoritmo de programación dinámica que encuentre el menor número de
palíndromos que forman una cadena dada. Por ejemplo, para ARACALACANA debería
devolver 3.


"""


def tabla_palindromos(palabra):
    n = len(palabra)
    pal = [[False] * n for _ in range(n)]

    for i in range(n):
        pal[i][i] = True

    for i in range(n - 1):
        pal[i][i + 1] = palabra[i] == palabra[i + 1]

    for largo in range(3, n + 1):
        for i in range(0, n - largo + 1):
            j = i + largo - 1
            pal[i][j] = palabra[i] == palabra[j] and pal[i + 1][j - 1]

    return pal



def palindromos_dinamico(palabra):
    n = len(palabra)
    pal = tabla_palindromos(palabra)
    if n == 0:
        return 0

    M = [float("inf")] * (n + 1)
    M[0] = 0

    for i in range(1, n + 1):
        for j in range(0, i):
            if pal[j][i - 1]:
                M[i] = min(M[i], M[j] + 1)

    return M[n]

print(palindromos_dinamico("ARACALACANA"))


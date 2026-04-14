
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

def palindromos_dinamico(palabra):
    if len(palabra) == 0:
        return 0
    if len(palabra) == 1:
        return 1
    letras_actuales = []
    palindromos = 0
    for letra in palabra:
        if len(letras_actuales) == 0:
            letras_actuales.append(letra)
        elif letra == letras_actuales[1:]:
            letras_actuales.append(letra)
        else:
            letras_actuales = []
            palindromos+=1
    return palindromos

print(palindromos_dinamico(ARACALACANA))
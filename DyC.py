# Se tiene una bolsa con n monedas de idéntica denominación,
# de las cuales exactamente una es falsa y se sabe que
# es más liviana que el resto.
# (Es la única forma de diferenciarla)
import random
import time


def moneda_falsa(monedas, cant_pesadas, indice=0):
    # Caso base
    if len(monedas) == 1:
        return monedas[0], cant_pesadas, indice

    mitad = len(monedas) // 2

    # Grupos iguales
    izquierda = monedas[:mitad]
    derecha = monedas[mitad : mitad * 2]

    # Moneda sobrante (si monedas es impar)
    resto = monedas[mitad * 2 :]

    # Calculamos pesos totales
    peso_izq = sum(izquierda)
    peso_der = sum(derecha)

    cant_pesadas += 1

    # La falsa está en la mitad más liviana o en el resto
    if peso_izq < peso_der:
        return moneda_falsa(izquierda, cant_pesadas, indice)
    elif peso_izq > peso_der:
        return moneda_falsa(derecha, cant_pesadas, indice + mitad)
    else:
        return moneda_falsa(resto, cant_pesadas, indice + mitad * 2)


def generar_monedas(n):
    monedas = [1] * n  # todas pesan 1
    falsa = random.randint(0, n - 1)
    monedas[falsa] = 0.99  # una más liviana
    return monedas


def prueba_tiempos(n):
    monedas = generar_monedas(n)
    cant_pesadas = 0

    inicio = time.time()
    moneda, cant_pesadas, indice = moneda_falsa(monedas, cant_pesadas)
    fin = time.time()

    tiempo = (fin - inicio) * 1000  # milisegundos

    return imprimiendo_mensaje(n, tiempo, moneda, cant_pesadas, indice)


def imprimiendo_mensaje(n, tiempo, moneda, cant_pesadas, indice):
    print(f"El tiempo para la prueba con {n} monedas fue de {tiempo:.10f}s")
    print(
        f"La moneda falsa encontrada pesa {moneda} y se encuentra en el índice {indice}"
    )
    print(f"Se pesaron un total de {cant_pesadas} veces")
    return


prueba_tiempos(1000000)

import random
import time

def generar_monedas(n):
    monedas = [100] * n
    falsa = random.randint(0, n - 1)
    monedas[falsa] = 99
    return monedas

# En vez de dividir en 2 grupos, divido en 3. La idea es aprovechar
# que una pesada tiene 3 resultados posibles (izquierda mas liviana,
# derecha mas liviana, o iguales), asi baja la cantidad de pesadas de log2(n) a log3(n).
def moneda_falsa(monedas, inicio=0, fin=None, pesadas=0):
    if fin is None:
        fin = len(monedas)

    cantidad = fin - inicio

    # Caso base: una moneda, es la falsa
    if cantidad == 1:
        return inicio, pesadas

    # Caso base: dos monedas, se pesan directamente
    if cantidad == 2:
        pesadas += 1
        if monedas[inicio] < monedas[inicio + 1]:
            return inicio, pesadas
        return inicio + 1, pesadas

    # Los dos primeros grupos son del mismo tamaño para poder compararlos.
    # Lo que sobra (0, 1 o 2 monedas) queda en el tercer grupo.
    tam = cantidad // 3
    f1 = inicio + tam
    f2 = f1 + tam

    peso1 = sum(monedas[inicio:f1])
    peso2 = sum(monedas[f1:f2])
    pesadas += 1

    # Uso indices (inicio, fin) en vez de cortar listas nuevas para
    # mantener el indice original de la moneda falsa.
    if peso1 < peso2:
        return moneda_falsa(monedas, inicio, f1, pesadas)
    if peso2 < peso1:
        return moneda_falsa(monedas, f1, f2, pesadas)
    return moneda_falsa(monedas, f2, fin, pesadas)


# Dejo una prueba
n = 1000000
monedas = generar_monedas(n)

inicio = time.time()
indice, pesadas = moneda_falsa(monedas)
fin = time.time()

tiempo = (fin - inicio) * 1000

print("n =", n)
print("Moneda falsa en el indice", indice, ", pesa", monedas[indice])
print("Pesadas:", pesadas)
print("Tiempo:", tiempo, "ms")

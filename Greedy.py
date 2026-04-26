INF = 15000


def leer_entero(mensaje):
    """Lee un entero desde consola con validación."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def leer_par(mensaje):
    """Lee un par de enteros desde consola con validación."""
    while True:
        try:
            a, b = map(int, input(mensaje).split())
            return a, b
        except ValueError:
            print("Error: debe ingresar dos números enteros separados por espacio.")


def cargar_datos_prueba():
    """
    Construye la matriz de costos usando la tabla dada en la consigna.
    """
    edges = [
        (1, 2, 66),
        (2, 3, 122),
        (2, 4, 126),
        (3, 4, 80),
        (3, 5, 148),
        (4, 5, 126),
        (5, 6, 49),
        (6, 7, 101),
        (7, 8, 69),
        (7, 9, 72),
        (8, 9, 45),
        (8, 11, 56),
        (11, 10, 30),
        (10, 9, 46)
    ]

    n = max(max(u, v) for u, v, _ in edges)
    cost = [[INF] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = 0

    for u, v, w in edges:
        cost[u-1][v-1] = w
        cost[v-1][u-1] = w

    return n, cost


def leer_grafo():
    """
    Solicita al usuario el grafo con validaciones de entrada.
    """
    print("\n¿Usar datos de prueba? (SI/NO): ", end="")
    modo = input().strip().upper()

    if modo == "SI":
        return cargar_datos_prueba()

    n = leer_entero("\nINGRESE EL NUMERO DE VERTICES: ")

    if n <= 0:
        print("Error: la cantidad de vértices debe ser positiva.")
        return leer_grafo()

    cost = [[0] * n for _ in range(n)]

    print("\nINGRESE EL CUADRO DE COSTOS (INGRESE 0 0 PARA TERMINAR)\n")

    while True:
        a, b = leer_par("EL EJE (A B): ")

        if a == 0 and b == 0:
            break

        if not (1 <= a <= n and 1 <= b <= n):
            print("Error: los vértices deben estar entre 1 y", n)
            continue

        w = leer_entero("COSTO DEL EJE: ")

        if w < 0:
            print("Error: el costo no puede ser negativo.")
            continue

        cost[a-1][b-1] = w

    # reemplazar 0 por INF
    for i in range(n):
        for j in range(n):
            if cost[i][j] == 0:
                cost[i][j] = INF

    # hacer matriz simétrica
    for i in range(n):
        for j in range(i):
            cost[i][j] = cost[j][i]

    return n, cost


def dijkstra(cost, v):
    """
    Calcula las distancias mínimas desde un vértice origen.
    """
    n = len(cost)

    dist = [0] * n
    sol = [0] * n

    for i in range(n):
        dist[i] = cost[v][i]
        sol[i] = 0

    sol[v] = 1
    dist[v] = 0

    for _ in range(n - 1):

        min_val = INF
        u = -1

        for j in range(n):
            if sol[j] == 0 and dist[j] <= min_val:
                min_val = dist[j]
                u = j

        sol[u] = 1

        for j in range(n):
            if dist[j] >= dist[u] + cost[u][j]:
                dist[j] = dist[u] + cost[u][j]

    return dist


def mostrar_resultados(dist, origen):
    """
    Imprime las distancias mínimas en formato tabular.
    """

    ancho = 10
    encabezado = f"{'SALIDA':<{ancho}}{'LLEGADA':<{ancho}}{'DISTANCIA':<{ancho}}"
    separador = "-" * (ancho * 3)

    print("\n" + encabezado)
    print(separador)

    contador = 0

    for i in range(len(dist)):
        if dist[i] < INF:
            print(f"{origen+1:<{ancho}}{i+1:<{ancho}}{dist[i]:<{ancho}}")
            contador += 1

def main():
    """
    Flujo principal con validaciones de entrada y modo de prueba.
    """
    n, cost = leer_grafo()

    while True:
        v = leer_entero("\nINGRESE EL VERTICE DE SALIDA: ") - 1

        if not (0 <= v < n):
            print("Error: vértice fuera de rango.")
            continue

        dist = dijkstra(cost, v)

        mostrar_resultados(dist, v)

        print("\nOTRA VEZ? (SI/NO): ", end="")
        res = input().strip().upper()
        if res == "NO":
            break


if __name__ == "__main__":
    main()
import pydot

def validar(val):
    flag = 0
    for x in val:
        if x != "0" and x != "1":
            flag = 1
    if flag == 1:
        print("Esta palabra no es válida, debe ser de la forma:")
        print("{0°n 1°n | n >= 0}")
        exit()
    else:
        posicion = val.find("1")
        recorre_unos = val[posicion:]
        recorre_ceros = val[:posicion]
        for y in recorre_unos:
            if y == "0":
                print("Esta palabra no es válida, debe ser de la forma:")
                print("{0°n 1°n | n >= 0}")
                exit()
        if len(recorre_unos) != len(recorre_ceros):
            print("Esta palabra no es válida, debe ser de la forma:")
            print("{0°n 1°n | n >= 0}")
            exit()

def automata_de_pila(val):
    pila = ["#"]
    alfabeto_pila = "a"
    print("Palabra del alfabeto: ", val)
    print("Estado inicial de la pila: ", pila)
    print()
    print()
    for i in val:
        if i == "0":
            pila.append(alfabeto_pila)
            print("Se lee un ", i, " en la pila y se INSERTA una a")
            print("pila: ", pila)
            print()
        if i == "1":
            if pila[-1] == "#":
                print("Error: La pila está vacía antes de leer un '1'")
                exit()
            pila.pop()
            print("Se lee un ", i, " en la pila y se EXTRAE una a")
            print("pila: ", pila)
            print()
    if pila[-1] != "#":
        print("Error: La pila no está vacía después de leer toda la cadena")
        exit()
    print("La cadena es válida según el autómata de pila")


print("Automata de pila de la forma:")
print("Alfabeto de la pila = {#,a}")
print("{0°n 1°n | n >= 0}")

valores = input("Escriba los valores:")
validar(valores)
automata_de_pila(valores)

# Crear un gráfico de la pila
graph = pydot.Dot(graph_type='digraph')
graph.add_edge(pydot.Edge("q0", "q0", label="0, Lambda ; a"))
graph.add_edge(pydot.Edge("q0", "q1", label="1, a ; Lambda"))
graph.add_edge(pydot.Edge("q1", "q1", label="1, a ; Lambda"))
#Doble circulo para el estado final

graph.add_edge(pydot.Edge("q1", "q2", label="Lambda, Z ; Lambda"))

graph.add_node(pydot.Node("q2", shape='doublecircle'))
graph.write_png('automatas-img/APD.png')

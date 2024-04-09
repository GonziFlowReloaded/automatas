import pydot

def validar(val: str):
    """
    Valida si la cadena de entrada es de la forma adecuada.

    La cadena debe estar compuesta únicamente de '0's y '1's, 
    y debe tener un número igual de '0's y '1's, o empezar con '1' y tener un número mayor de '1's que de '0's.

    Si la cadena no cumple con estas condiciones, se imprime un mensaje de error y se termina el programa.

    Parámetros:
        val (str): La cadena de entrada a validar.
    """
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

def automata_de_pila(val: str):
    """
    Implementa un autómata de pila para validar si una cadena cumple con la forma especificada.

    El autómata de pila lee una cadena de entrada compuesta únicamente de '0's y '1's, 
    y verifica si la cantidad de '0's es igual a la cantidad de '1's o si la cadena empieza con '1' 
    y tiene más '1's que '0's.

    Si la cadena cumple con las condiciones, se imprime un mensaje indicando que es válida según el autómata de pila.

    Parámetros:
        val (str): La cadena de entrada a verificar.
    """
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

# # Crear un gráfico de la pila
# graph = pydot.Dot(graph_type='digraph')
# graph.add_edge(pydot.Edge("q0", "q0", label="0, Lambda ; a"))
# graph.add_edge(pydot.Edge("q0", "q1", label="1, a ; Lambda"))
# graph.add_edge(pydot.Edge("q1", "q1", label="1, a ; Lambda"))
# #Doble circulo para el estado final

# graph.add_edge(pydot.Edge("q1", "q2", label="Lambda, Z ; Lambda"))

# graph.add_node(pydot.Node("q2", shape='doublecircle'))
# graph.write_png('automatas-img/APD.png')

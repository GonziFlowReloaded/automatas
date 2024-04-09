from typing import Union, Callable
import pydot

def delta_perro(q: str, i: str) -> Union[str, None]:
    """
    Función de transición para el autómata específico que acepta "perro" o "perrooooo".

    Parámetros:
        q (str): Estado actual del autómata.
        i (str): Símbolo de entrada.

    Devoluciones:
        Union[str, None]: Estado siguiente del autómata si existe una transición para el símbolo de entrada,
                           None si no hay transición definida para el estado y el símbolo de entrada.
    """
    # Tabla de transición para el autómata específico que acepta "perro" o "perrooooo"
    tabla_de_transicion_perro = {
        ("q0", "p"): "q1",
        ("q1", "e"): "q2",
        ("q2", "r"): "q3",
        ("q3", "r"): "q4",
        ("q4", "o"): "q5",
        ("q5", "o"): "q5",  # Transición adicional para permitir múltiples 'o'
    }
    return tabla_de_transicion_perro.get((q, i), None)

class AutomataPerro:
    """
    Clase que representa un autómata específico para reconocer la cadena "perro" o "perrooooo".

    Atributos:
        estados (set): Conjunto de estados del autómata.
        alfabeto (set): Conjunto de símbolos del alfabeto.
        estado_inicial (str): Estado inicial del autómata.
        estados_finales (set): Conjunto de estados finales del autómata.
        transicion (Callable): Función de transición del autómata.
    """
    def __init__(
            self,
            Q: set = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
            sigma: set = {'p', 'e', 'r', 'o'},
            q0: str = 'q0',
            F: set = {'q5'},
            delta: Callable = delta_perro
    ):
        self.estados = Q
        self.alfabeto = sigma
        self.estado_inicial = q0
        self.estados_finales = F
        self.transicion = delta
    
    def __call__(self, q, i) -> Union[str, None]:
        """
        Método para realizar una transición en el autómata.

        Parámetros:
            q (str): Estado actual del autómata.
            i (str): Símbolo de entrada.

        Devoluciones:
            Union[str, None]: Estado siguiente del autómata si existe una transición para el símbolo de entrada,
                               None si no hay transición definida para el estado y el símbolo de entrada.
        """
        return self.transicion(q, i)
    
    def es_estado_final(self, q) -> bool:
        """
        Comprueba si un estado dado es un estado final del autómata.

        Parámetros:
            q (str): Estado a verificar.

        Devoluciones:
            bool: True si el estado es un estado final, False en caso contrario.
        """
        return q in self.estados_finales
    

def d_reconocer_perro(cinta: str, automata: AutomataPerro) -> bool:
    """
    Función que verifica si una cadena es aceptada por el autómata específico para "perro" o "perrooooo".

    Parámetros:
        cinta (str): Cadena de entrada a verificar.
        automata (AutomataPerro): Autómata para la verificación.

    Devoluciones:
        bool: True si la cadena es aceptada por el autómata, False en caso contrario.
    """
    indice  = 0
    estado_actual = automata.estado_inicial
    while True:
        if indice == len(cinta):
            if automata.es_estado_final(estado_actual):
                return True
            else:
                return False
        elif not automata(estado_actual, cinta[indice]):
            return False
        else:
            print(f"δ({estado_actual}, {cinta[indice]}) = {automata(estado_actual, cinta[indice])}")
            estado_actual = automata(estado_actual, cinta[indice])
            indice += 1


def generate_automaton_graph():
    """
    Genera un diagrama de grafos representando el autómata específico para "perro" o "perrooooo".
    """
    automaton = AutomataPerro()
    graph = pydot.Dot(graph_type='digraph')
    
    for state in automaton.estados:
        if state in automaton.estados_finales:
            node = pydot.Node(state, shape='doublecircle')
        else:
            node = pydot.Node(state)
        graph.add_node(node)
    
    for state in automaton.estados:
        for symbol in automaton.alfabeto:
            next_state = automaton(state, symbol)
            if next_state:
                edge = pydot.Edge(state, next_state, label=symbol)
                graph.add_edge(edge)
    
    graph.write_png('automatas-img/AFD.png')


automata_perro = AutomataPerro()
cinta_perro = "perrooooooooooooooooooo"

if d_reconocer_perro(cinta_perro, automata_perro):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena no es aceptada por el autómata.")

generate_automaton_graph()

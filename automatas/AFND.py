from typing import Union, Callable
import pydot

def delta_perro(q: str, i: str) -> Union[str, None]:
    # Tabla de transición para el autómata específico que acepta "perro" o "perrooooo"
    tabla_de_transicion_perro = {
        ("q0", "p"): "q1",
        ("q1", "e"): "q2",
        ("q2", "r"): "q3",
        ("q3", "r"): "q4",
        ("q4", "o"): "q5",
        ("q4", "a"): "q6",
        ("q5", "o"): "q5", 
        ("q6", "a"): "q6",
    }
    return tabla_de_transicion_perro.get((q, i), None)

class AutomataPerro:
    def __init__(
            self,
            Q: set = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
            sigma: set = {'p', 'e', 'r', 'o', 'a'},
            q0: str = 'q0',
            F: set = {'q5'},
            delta: Callable = delta_perro
    ):
        # Inicialización de los atributos del autómata específico para "perro" o "perrooooo"
        self.estados = Q
        self.alfabeto = sigma
        self.estado_inicial = q0
        self.estados_finales = F
        self.transicion = delta
    
    def __call__(self, q, i) -> Union[str, None]:
        return self.transicion(q, i)
    
    def es_estado_final(self, q) -> bool:
        return q in self.estados_finales
    

def d_reconocer_perro(cinta: str, automata: object) -> bool:
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


automata_perro = AutomataPerro()
cinta_perro = "perrooooooooooooooooooo"

if d_reconocer_perro(cinta_perro, automata_perro):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena no es aceptada por el autómata.")

def generate_automaton_graph():
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
    
    graph.write_png('automatas-img/AFND.png')


generate_automaton_graph()
from typing import Union, Callable

def delta(q: str, i: str) -> Union[str, None]:
    # Tabla de transición representada como un diccionario
    tabla_de_transicion = {
        ("q0", "b"): "q1", 
        ("q1", "a"): "q2", 
        ("q2", "a"): "q3", 
        ("q3", "a"): "q3", 
        ("q3", "!"): "q4", 
    }
    return tabla_de_transicion.get((q, i), None)

class Automata:
    def __init__(
            self,
            Q: set = {'q0', 'q1', 'q2', 'q3', 'q4'},
            sigma: set = {'a','b','!'},
            q0: str = 'q0',
            F: set = {'q4'},
            delta: Callable = delta
    ):
        # Inicialización de los atributos del autómata
        self.estados = Q
        self.alfabeto = sigma
        self.estado_inicial = q0
        self.estados_finales = F
        self.transicion = delta
    
    def __call__(self, q, i) -> Union[str, None]:
        return self.transicion(q, i)
    
    def es_estado_final(self, q) -> bool:
        return q in self.estados_finales
    

def d_reconocer(cinta: str, automata: object) -> bool:
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


automata = Automata()
cinta = "baa!"

if d_reconocer(cinta, automata):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena no es aceptada por el autómata.")

from typing import Union, Callable

def delta_binario(q: str, i: str) -> Union[str, None]:
    # Tabla de transición para el autómata específico que acepte cualquier cadena que contenga 1 o 0
    tabla_de_transicion_binario = {
        ("q0", "0"): "q1",
        ('q0', '1'): 'q2',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q2',
    }
    return tabla_de_transicion_binario.get((q, i), None)

class AutomataClase:
    def __init__(
            self,
            Q: set = {'q0', 'q1', 'q2'},
            sigma: set = {'0', '1'},
            q0: str = 'q0',
            F: set = {'q2'},
            delta: Callable = delta_binario
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
    

def d_reconocer_binario(cinta: str, automata: object) -> bool:
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


automata_perro = AutomataClase()
cinta_perro = "100000001111"

if d_reconocer_binario(cinta_perro, automata_perro):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena no es aceptada por el autómata.")

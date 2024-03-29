import matplotlib.pyplot as plt
import networkx as nx

def dibujar_automata(estado_inicial, estados_aceptacion, transiciones):
    G = nx.DiGraph()

    # Agregar nodos
    for estado in transiciones.keys():
        G.add_node(estado)
    
    # Agregar arcos
    for estado, transicion in transiciones.items():
        for simbolo, destino in transicion.items():
            etiqueta = simbolo
            if estado == destino:
                # Si es una transición que se autoreferencia, agregamos la letra por la cual se autoreferencia
                etiqueta = f"{etiqueta}({estado})"
            G.add_edge(estado, destino, label=etiqueta)
    
    # Establecer el diseño del gráfico
    pos = nx.spring_layout(G)

    # Dibujar nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos)

    # Dibujar arcos y etiquetas
    nx.draw_networkx_edges(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    

    # Marcar estado inicial y estados de aceptación
    plt.gca().add_patch(plt.Circle(pos[estado_inicial], 0.1, color='r', fill=True))
    for estado_aceptacion in estados_aceptacion:
        plt.gca().add_patch(plt.Circle(pos[estado_aceptacion], 0.1, color='g', fill=True))

    plt.axis('off')
    plt.show()

# Definición del autómata
estado_inicial = 'q0'
estados_aceptacion = ['q5']
transiciones = {
    'q0': {'p': 'q1'},
    'q1': {'e': 'q2'},
    'q2': {'r': 'q3'},
    'q3': {'r': 'q4'},
    'q4': {'o': 'q5', 'r': 'q4'},  # Transición adicional para permitir múltiples 'o'
}

# Dibujar el autómata
dibujar_automata(estado_inicial, estados_aceptacion, transiciones)

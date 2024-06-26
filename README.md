# Autómatas y Validación de Cadenas

Este repositorio contiene implementaciones de autómatas y funciones para validar cadenas en Python.

## Contenido

- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Detalles de Implementación](#detalles-de-implementación)
- [Ejemplos](#ejemplos)

## Requisitos

- Python 3.x
- pydot (para generar gráficos de autómatas)

## Instrucciones de Uso

1. Clona este repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git


2. Instala las dependencias:

pip install -r requirements.txt


3. Ejecuta los scripts Python según sea necesario.

## Detalles de Implementación

### Validación de Cadenas

El archivo `validacion_cadenas.py` contiene funciones para validar cadenas según ciertas reglas especificadas. 

- La función `validar(val)` verifica si una cadena dada es de la forma especificada, donde debe tener un número igual de '0's y '1's, o empezar con '1' y tener un número mayor de '1's que de '0's.

### Autómata de Pila

El archivo `automata_pila.py` implementa un autómata de pila para validar si una cadena cumple con las condiciones especificadas.

- La función `automata_de_pila(val)` implementa el autómata de pila y verifica si la cadena dada cumple con las condiciones requeridas.

### Generación de Gráficos

Ambos scripts también incluyen funciones para generar gráficos de los autómatas.

## Ejemplos

Puedes encontrar ejemplos de uso en los propios scripts o ejecutarlos con datos de entrada personalizados.


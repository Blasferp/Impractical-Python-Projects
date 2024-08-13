"Generador de de nombres divertidos con Primer nombre, Nombre del medio y Apellido"

import string

from pprint import pprint
from collections import defaultdict

def main():
    """
    La función main ejecuta el proceso principal del programa:
    1. Cuenta las letras en el texto dado.
    2. Imprime el diccionario de letras y sus apariciones.
    
    """

    # Texto de ejemplo
    texto = 'Like the castle in its corner in a medieval game, I foresee terrible \
    trouble and I stay here just the same.'
    # Crear un defaultdict con listas predeterminadas
    dicc = defaultdict(list)

    # Iterar sobre el texto
    for i in texto.lower():
        # Convertir a minúsculas para que las letras mayúsculas y minúsculas se cuenten igual
        if i in string.ascii_lowercase:  # Verificar si el carácter es una letra
            dicc[i].append(i)  # Agregar la letra a la lista correspondiente
    # Imprimir el diccionario de listas usando pprint
    pprint(dict(dicc), width=300)  # Convertimos defaultdict a dict para una impresión más limpia

if __name__ == "__main__":
    main()

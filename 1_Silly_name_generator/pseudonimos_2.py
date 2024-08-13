"""Genera nombres divertidos combinando nombres de 3 listas separadas."""
import sys
import random

def main():
    """
    Elige nombres al azar de 3 tuplas de nombres (nombres, segundos nombres y apellidos) y los imprime en la pantalla.

    La función sigue los siguientes pasos:
    1. Muestra un mensaje de bienvenida.
    2. Elige un nombre al azar de la lista de nombres.
    3. Elige un segundo nombre al azar con una probabilidad del 50%.
    4. Elige un apellido al azar de la lista de apellidos.
    5. Imprime el nombre completo en la pantalla.
    6. Pregunta al usuario si desea generar otro nombre o salir.
    7. Repite el proceso hasta que el usuario decida salir.
    """
    # Mensaje de bienvenida
    print("Bienvenido al Generador de Nombres Divertidos.\n")
    
    # Tuplas de nombres
    first_names = ('Baby Oil', 'Bad News', 'Big Burps', 'Bill', 'Bob', 'Bowel Noises', 
                   'Boxelder', 'Bud', 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 
                   'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
                   'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis', 'Dicman', 'Elphonso',
                   'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
                   'Huggy', 'Ignatious', 'Jimbo', 'Johnny', 'Lemongrass', 'Lil Debil',
                   'Longbranch', 'Mergatroid', 'Oil-Can', 'Oinks', 'Old Scratch', 
                   'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
                   'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', 'Skidmark', 
                   'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout', 
                   'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
                   'Winston', 'Worms')

    middle_names = ("'Beenie-Weenie'", "'Stinkbug'", "'Lite'", "'Jazz Hands'",
                    "'Pottin Soil'", "'The Squirts'", 'The Big News', 'Grunts', 
                    'Tinkie Winkie', 'Oil Can', 'Lunch Money', 'Mr Peabody')

    last_names = ('Smith', 'Jones', 'Brown', 'Johnson', 'Williams', 'Miller', 'Davis',
                  'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor',
                  'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson',
                  'White', 'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark', 'Lewis',
                  'Robinson', 'Walker', 'Perez', 'Hall', 'Young', 'Allen', 'Sanchez',
                  'Wright', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson',
                  'Hill', 'Ramirez', 'Campbell', 'Mitchell', 'Roberts', 'Carter',
                  'Phillips', 'Evans', 'Turner', 'Torres', 'Parker', 'Collins', 'Edwards')

    while True:
        # Elegir un nombre al azar de la lista de nombres
        first_name = random.choice(first_names)
        # Elegir un segundo nombre al azar con una probabilidad del 50%
        middle_name = random.choice(middle_names) if random.choice([True, False]) else ''
        # Elegir un apellido al azar de la lista de apellidos
        last_name = random.choice(last_names)
        
        # Construir el nombre completo
        if middle_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"

        # Imprimir el nombre completo en la pantalla
        print("\n\n")
        print(full_name)
        print("\n\n")

        # Preguntar al usuario si desea intentar de nuevo o salir
        try_again = input(
        "\n\n¿Intentar de nuevo? (Presiona Enter para continuar, "
        "o 'n' para salir)\n "
    )

        if try_again.lower() == "n":
            break

    # Mensaje final antes de salir
    input("\nPresiona Enter para salir.")

if __name__ == "__main__":
    main()

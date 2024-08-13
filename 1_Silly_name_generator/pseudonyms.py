"""Genera nombres divertidos combinando nombres de 2 listas separadas."""
import sys
import random

def main():
    """
    Elige nombres al azar de 2 tuplas de nombres y los imprime en la pantalla.
    
    La función sigue los siguientes pasos:
    1. Muestra un mensaje de bienvenida.
    2. Elige un nombre al azar de la lista de nombres de pila (first).
    3. Elige un nombre al azar de la lista de apellidos (last).
    4. Imprime el nombre completo en la salida de error estándar.
    5. Pregunta al usuario si desea generar otro nombre o salir.
    6. Repite el proceso hasta que el usuario decida salir.
    """
    print("Bienvenido al 'Generador de Nombres Divertidos'.\n")
    print("Un nombre que Sean podría elegir para Gus:\n\n")

    # Tuplas de nombres
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
            'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        # Elegir un nombre al azar de cada tupla
        first_name = random.choice(first)
        last_name = random.choice(last)

        # Imprimir el nombre completo en la salida de error estándar
        print("\n\n")
        print(f"{first_name} {last_name}", file=sys.stderr)
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

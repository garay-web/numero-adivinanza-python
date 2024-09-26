import random


def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    # Primeras líneas ddel juego donde se dda la bienvenida
    print("¡Bienvenido al juego de adivinanza del número")
    print("Debes adivinar un número del 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un número
        adivinanza = input("Introduzca un número del 1 al 100 :  ")
        # Verificamos que la entrada sea un número
        if adivinanza.isdigit():
            # En el caso de que sea un número lo convertimo en un entero
            adivinanza = int(adivinanza)
            intentos += 1
            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"El número {adivinanza} es el secreto y lo lograste en {intentos} intentos.-"
                )

        else:
            print("Introduzca un número del 1 al 100")


juego_adivinanza()

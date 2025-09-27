from pyfiglet import Figlet
import random

def texto():
    # Crear objeto Figlet
    figlet = Figlet()

    # Obtener todas las fuentes disponibles
    fuentes = figlet.getFonts()

    # Pedir al usuario la fuente
    fuente_usuario = input("Ingrese el nombre de la fuente (Enter para aleatoria): ").strip()

    if fuente_usuario == "":
        fuente_seleccionada = random.choice(fuentes)
        print(f"No ingresó fuente, se eligió aleatoriamente: {fuente_seleccionada}")
    else:
        if fuente_usuario in fuentes:
            fuente_seleccionada = fuente_usuario
        else:
            print("Fuente no válida. Se usará una aleatoria.")
            fuente_seleccionada = random.choice(fuentes)

    # Configurar fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    # Pedir el texto al usuario
    texto = input("Ingrese el texto a imprimir: ")

    # Mostrar el resultado
    print("\nResultado:\n")
    print(figlet.renderText(texto))

texto()

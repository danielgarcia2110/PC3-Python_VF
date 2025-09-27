# Problema 1
while True:
    try:
        fraccion = input("Ingrese la fracción en formato X/Y: ")
        x, y = fraccion.split("/")
        x = float(x)
        y = float(y)


        # validaciones
        if y == 0:
            print("Error: el denominador no puede ser 0. ZeroDivisionError")
            continue
        if x != int(x) or y != int(y):
            print("Error: solo se permiten enteros positivos. ValueError")
            continue

        porcentaje = round((x / y) * 100)

        # validar rango válido
        if porcentaje < 0 or porcentaje > 100:
            print("Fracción fuera de rango. Intente de nuevo.")
            continue  # vuelve a pedir input

        # condiciones de salida
        if porcentaje <= 1:
            print("E")
        elif porcentaje >= 99:
            print("F")
        else:
            print(f"{porcentaje}%")
        break   # salir del bucle si es válido

    except ValueError:
        # si no se pueden convertir a enteros o formato inválido
        continue
    except ZeroDivisionError:
        # seguridad extra aunque ya controlamos y==0
        continue

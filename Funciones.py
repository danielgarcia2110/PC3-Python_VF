# Problema 2
# Escribir un programa que permita ingresar el nombre completo de n alumnos y sus 3 notas.
def cargar_alumnos():
    alumnos = []
    try:
        n = int(input("¿Cuántos alumnos desea ingresar? "))
    except ValueError:
        print("Error: debe ingresar un número entero.")
        return []

    for i in range(n):
        print(f"\nAlumno {i+1}:")
        nombre = input("Ingrese el nombre completo: ")

        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Error: la nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: debe ingresar un número válido.")

        alumnos.append({
            "nombre": nombre,
            "notas": notas
        })
    print("\nNombres de los alumnos ingresados:")
    for i in range(len(alumnos)):
        print(alumnos[i]['nombre'])
    return alumnos

cargar_alumnos()

# Problema 3
# Definición de la clase Rectangulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


# Definición de la clase Cuadrado (hereda de Rectangulo)
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # un cuadrado es un rectángulo con largo = ancho = lado
        super().__init__(lado, lado)



lado = int(input("Ingrese el largo del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))

# Crear un objeto de tipo Rectangulo
rect = Rectangulo(lado, ancho)
print(f"Área del rectángulo: {rect.calcular_area()}")

# Crear un objeto de tipo Cuadrado
cuad = Cuadrado(lado)
print(f"Área del cuadrado: {cuad.calcular_area()}")


# Problema 4
def evaluar_alumnos(lista_alumnos):
    aprobados = 0
    desaprobados = 0

    for alumno in lista_alumnos:
        try:
            notas = alumno["notas"]

            # Validación: deben ser exactamente 3 notas
            if len(notas) != 3:
                raise ValueError(f"El alumno {alumno['nombre']} no tiene 3 notas.")

            # Calcular promedio (asegurando que son numéricas)
            promedio = sum(float(n) for n in notas) / 3

            if promedio >= 4:
                aprobados += 1
            else:
                desaprobados += 1

        except ValueError as e:
            print(f"Error en datos del alumno {alumno.get('nombre','?')}: {e}")
        except Exception as e:
            print(f"Error inesperado en alumno {alumno.get('nombre','?')}: {e}")
    print(f"\nTotal de alumnos aprobados: {aprobados}")
    print(f"Total de alumnos desaprobados: {desaprobados}")
    return aprobados, desaprobados

evaluar_alumnos(cargar_alumnos())

# Problema 5
def calcular_promedios(lista_alumnos):
    resultados = []
    for alumno in lista_alumnos:
        notas = alumno["notas"]      
        promedio = sum(float(n) for n in notas) / 3
        print(f"Alumno: {alumno['nombre']} - Promedio: {promedio:.2f}")
        resultados.append({
                "nombre": alumno["nombre"],
                "promedio": promedio
        })
    return resultados

calcular_promedios(cargar_alumnos())

# Problema 6
def mejor_peor_promedio(promedios):
    
    # Usamos la función que ya devuelve nombre y promedio
    mejor = max(promedios, key=lambda x: x["promedio"])
    peor = min(promedios, key=lambda x: x["promedio"])

    print(f"\nEl alumno con el promedio más alto es: {mejor['nombre']} ({mejor['promedio']:.2f})")
    print(f"El alumno con el promedio más bajo es: {peor['nombre']} ({peor['promedio']:.2f})")

    return mejor, peor

mejor_peor_promedio(calcular_promedios(cargar_alumnos()))

# Problema 7
def buscar_alumno(lista_alumnos, nombre_busqueda):
    resultados = []
    promedios = calcular_promedios(lista_alumnos)  
    for alumno in promedios:
        # Búsqueda insensible a mayúsculas/minúsculas
        if nombre_busqueda.lower() in alumno["nombre"].lower():
            notas = next(item["notas"] for item in lista_alumnos if item["nombre"] == alumno["nombre"])
            resultados.append({
                "nombre": alumno["nombre"],
                "notas": notas,
                "promedio": alumno["promedio"]
            })

    if resultados:
        print("\n🔎 Resultados de la búsqueda:")
        for r in resultados:
            print(f"Alumno: {r['nombre']} | Notas: {r['notas']} | Promedio: {r['promedio']:.2f}")
    else:
        print("\n⚠️ No se encontraron alumnos con ese nombre.")

    return resultados

buscar_alumno(cargar_alumnos(), input("Ingrese el nombre del alumno a buscar: "))
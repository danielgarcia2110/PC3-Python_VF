import requests
import zipfile
import os

# URL de la imagen
url = "https://static.wikia.nocookie.net/dragonball/images/1/18/Goku_MUI_manga_color.jpg/revision/latest/scale-to-width/360?cb=20210526092301"

# Nombre de la imagen y del zip
nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen.zip"

# Descargar la imagen
try:
    print("Descargando imagen...")
    response = requests.get(url)
    response.raise_for_status()

    with open(nombre_imagen, "wb") as f:
        f.write(response.content)
    print(f"Imagen guardada como {nombre_imagen}")

except requests.RequestException as e:
    print(f"Error al descargar la imagen: {e}")


# Crear un archivo ZIP y almacenar la imagen
with zipfile.ZipFile(nombre_zip, "w") as zipf:
    zipf.write(nombre_imagen)
print(f"Imagen comprimida en {nombre_zip}")


# Extraer (unzip) el archivo
carpeta_salida = "imagenes_extraidas"
os.makedirs(carpeta_salida, exist_ok=True)

with zipfile.ZipFile(nombre_zip, "r") as zipf:
    zipf.extractall(carpeta_salida)
print(f"Imagen extraída en la carpeta: {carpeta_salida}")

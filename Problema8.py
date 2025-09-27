import requests
import pandas as pd
import time

def obtener_tipo_cambio(year=2025):
    """
    Obtiene el tipo de cambio de la SUNAT para un año completo (mes por mes).
    Devuelve un DataFrame con las columnas: fecha, compra, venta, diferencia.
    """
    datos = []
    for mes in range(1, 10):
        print(f"📡 Obteniendo datos del mes {mes}...")
        url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={year}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Guardamos en lista
            for registro in data:
                fecha = registro["fecha"]
                compra = float(registro["compra"])
                venta = float(registro["venta"])
                diferencia = venta - compra
                datos.append([fecha, compra, venta, diferencia])
        
            time.sleep(2)

        except requests.RequestException as e:
            print(f"Error al obtener datos para {mes}/{year}: {e}")

    # Convertimos a DataFrame
    df = pd.DataFrame(datos, columns=["fecha", "compra", "venta", "diferencia"])
    return df


def analizar_tipo_cambio(df):
    """
    Analiza el DataFrame y devuelve las fechas de:
    - compra mínima
    - venta máxima
    - diferencia máxima
    """
    fecha_compra_min = df.loc[df["compra"].idxmin(), ["fecha", "compra"]]
    fecha_venta_max = df.loc[df["venta"].idxmax(), ["fecha", "venta"]]
    fecha_diferencia_max = df.loc[df["diferencia"].idxmax(), ["fecha", "diferencia"]]

    return fecha_compra_min, fecha_venta_max, fecha_diferencia_max


# --- EJECUCIÓN ---

df = obtener_tipo_cambio(2025)

if not df.empty:
    print("\nDatos obtenidos:")
    print(df.head())

    compra_min, venta_max, dif_max = analizar_tipo_cambio(df)

    print("\nResultados:")
    print(f"Fecha con compra mínima: {compra_min['fecha']} (S/ {compra_min['compra']})")
    print(f"Fecha con venta máxima: {venta_max['fecha']} (S/ {venta_max['venta']})")
    print(f"Fecha con mayor diferencia compra-venta: {dif_max['fecha']} (Diferencia: S/ {dif_max['diferencia']})")
else:
    print("No se pudieron obtener datos del tipo de cambio.")

import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    return pd.read_csv(ruta_archivo)


datos = cargar_datos("estadisticas.csv")


def punto1(df: pd.DataFrame):
    df = df[(df["TotalIntegrantesGrupoFamiliar"] >= 0) & (df["TotalIntegrantesGrupoFamiliar"] < 11)]
    inf = df['TotalIntegrantesGrupoFamiliar'].value_counts().sort_index()
    inf.plot.bar()
    plt.xlabel("Integrantes por familia")
    plt.ylabel("Número de Familias")
    plt.show()


punto1(datos)


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    return pd.read_csv(ruta_archivo)


datos = cargar_datos("winequality-red.csv")


def punto3(datos: pd.DataFrame):
    quality = sorted(datos["quality"].unique())
    total = []
    for q in quality:
        cant = 0
        for wineQ in datos["quality"]:
            if wineQ == q:
                cant += 1
        total.append(cant)
        print("Quality:", q, "Total:", cant)
    plt.pie(total, labels=quality)
    plt.show()

#punto3(datos)

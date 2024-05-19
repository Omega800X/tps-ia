import pandas as pd
from sklearn.preprocessing import LabelEncoder

# a) Carga el archivo car.csv en un DataFrame y mostrar las primeras 5 filas.
print(10 * "-", "PUNTO A", 10 * "-")
col_names = [
    "buying",
    "maintenance",
    "doors",
    "persons",
    "luggage_boot",
    "safety",
    "class",
]
df = pd.read_csv("car.csv", header=0, names=col_names)
print(df.head(5))

# b) Mostrar la información básica del DataFrame
print(10 * "-", "PUNTO B", 10 * "-")
print(df.info())

# c) Mostrar las estadísticas básicas del DataFrame
print(10 * "-", "PUNTO C", 10 * "-")
print(df.describe())

# d) Seleccionar las columnas del DataFrame y mostrarlas por pantalla.
print(10 * "-", "PUNTO D", 10 * "-")
print(df.columns)

# e) Filtra las filas del DataFrame que cumplan con la condición persons=2.
print(10 * "-", "PUNTO E", 10 * "-")
print(df[df["persons"] == "2"])

# f) Agrupa el DataFrame por una columna específica y muestra la media de otra columna.
print(10 * "-", "PUNTO F", 10 * "-")
df["persons"] = pd.to_numeric(df["persons"], errors="coerce")
promedio = df.groupby("safety")["persons"].mean(numeric_only=True)
print(promedio)

# g) Convierte la variable objetivo a una variable binaria usando Label Encoding.
print(10 * "-", "PUNTO G", 10 * "-")

print(10 * "-", "TARGET BEFORE", 10 * "-")
print(df["class"])
le = LabelEncoder()
df["class"] = le.fit_transform(df["class"])

print(10 * "-", "TARGET AFTER", 10 * "-")
print(df["class"])

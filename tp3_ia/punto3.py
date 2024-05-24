import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import numpy as np

# (a) Utilizar el 70 % de los datos para entrenamiento y el 30 % restante para testeo.
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

dataset = pd.read_csv("car.csv", header=0, names=col_names)
print(dataset.head(243))

dataset["class"] = dataset["class"].apply(lambda x: 0 if x == "unacc" else 1)

print(dataset.tail())

features_cols = ["buying", "maintenance", "doors", "persons", "luggage_boot", "safety"]

le = LabelEncoder()

for col in col_names:
    dataset[col] = le.fit_transform(dataset[col])

x = dataset[features_cols]
y = dataset["class"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=444
)

model = DecisionTreeClassifier(random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


# (b) Evaluar la precisión del modelo utilizando Accuracy.
print(10 * "-", "PUNTO B", 10 * "-")
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


# (c) A partir de la métrica obtenida: ¿Qué podemos decir del modelo creado?
print(10 * "-", "PUNTO C", 10 * "-")
"""
Probando con diferentes valores de random_state tanto para el clasificador
como para el split se obtuvieron valores de accuracy muy cercanos al 1.0.
Por ejemplo con random_state=1 la exactitud del modelo fue de
0.9826589595375722 por lo que el modelo realizó ~98% de predicciones
correctas.
Con esto podemos decir que el modelo es bueno para predecir si un automóvil
es aceptable o no a partir de las características dadas.
"""

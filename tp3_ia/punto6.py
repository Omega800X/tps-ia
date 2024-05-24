import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Dataset ClientesEnLinea.csv
# Crear un modelo de Regresión Logística utilizando el dataset ClientesEnLinea.csv que cuenta con in-
# formación de clientes que compran o no ciertos productos en línea para ello contamos con información
# sobre el género, la edad y el salario estimado, clasificando a los clientes con 0 y 1 si no compró o si
# compró respectivamente.
# Utilizar como métrica comparativa el promedio de una validación cruzada K-fold con 5 folds para
# entrenamiento y testeo.

df = pd.read_csv("ClientesEnLinea.csv")

print(df.head())
print("\n")

le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])

print(df.head())
print("\n")

x = df[["Sex", "Edad", "SalarioEstimado"]]
y = df["Compra"]


model = LogisticRegression(max_iter=10000)


# (a) ¿Cómo se comporta el modelo si consideramos todos los predictores?
print(10 * "-", "PUNTO A", 10 * "-")
scores = cross_validate(
    model, x, y, scoring=["accuracy", "precision", "f1", "recall"], cv=5
)

print("Accuracies:", scores["test_accuracy"])
print("Precisions:", scores["test_precision"])
print("Recalls:", scores["test_recall"])
print("F1s:", scores["test_f1"])

print("Mean accuracy:", scores["test_accuracy"].mean())
print("Mean Precision:", scores["test_precision"].mean())
print("Mean Recall:", scores["test_recall"].mean())
print("Mean F1:", scores["test_f1"].mean())

"""
Si consideramos todos los predictores, tras la validación cruzada de 5
K-Folds el modelo muestra:
- Una exactitud promedio de ~82%
- Una precisión promedio de ~80%
- Un recall promedio de ~68%
- Un F1 promedio de ~70%
Por lo que el modelo podría considerarse que no es tan bueno a la hora de
clasificar a los clientes.
"""

# (b) ¿Qué sucede cuando solo consideramos como predictores Sexo y Edad?

print("\n")
print(10 * "-", "PUNTO B", 10 * "-")

mod_x = x.drop(["SalarioEstimado"], axis=1)

print("mod_x: \n", mod_x.head())
print("\n")

scores = cross_validate(
    model, mod_x, y, scoring=["accuracy", "precision", "f1", "recall"], cv=5
)

print("Accuracies:", scores["test_accuracy"])
print("Precisions:", scores["test_precision"])
print("Recalls:", scores["test_recall"])
print("F1s:", scores["test_f1"])

print("Mean accuracy:", scores["test_accuracy"].mean())
print("Mean Precision:", scores["test_precision"].mean())
print("Mean Recall:", scores["test_recall"].mean())
print("Mean F1:", scores["test_f1"].mean())


"""
Cuando sólo consideramos como predictores el Sexo y la Edad del cliente
obtenemos resultados muy similares a los obtenidos utilizando todos los
predictores. A partir de esto podemos observar que el predictor "SalarioEstimado"
no aporta mucho a la hora de realizar las predicciones.
"""

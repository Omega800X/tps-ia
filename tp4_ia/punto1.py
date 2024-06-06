import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Dataset: autenticacion_moneda.csv
# El dataset cuenta con datos obtenidos a partir de imágenes de diferentes monedas tanto genuinas como
# falsas. Tenemos información sobre la varianza, asimetría, curtosis, entropía de la imagen y la clase a la
# que pertenece (genuinas o falsas).

dataset = pd.read_csv("autenticacion_moneda.csv", header=0, names=["Variance","Skewness","Curtosis","Entropy","Clase"])

X = dataset.drop(columns=["Clase"])
y = dataset["Clase"]




# a) Obtener la curva Elbow para determinar la cantidad de arboles. Adjuntar imagen.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)
rango_arboles = range(1, 101)
accuracies = []

for num_arboles in rango_arboles:
    model = RandomForestClassifier(n_estimators=num_arboles, random_state=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))

plt.plot(rango_arboles, accuracies)
plt.xlabel("Número de árboles")
plt.ylabel("Accuracy score")
plt.title("Curva Elbow")
plt.show()

# b) En un mismo código fuente .py hacer un clasificador por Regresión Logística y un clasificador
# por Random Forest conforme a lo que indico en el punto anterior. Utilizar validación cruzada
# K-fold con 5 folds para entrenamiento y testeo.
clasificador_rl = LogisticRegression(random_state=100)
clasificador_rf = RandomForestClassifier(n_estimators=3, random_state=100)

metricas_rl = cross_validate(clasificador_rl, X, y, scoring=["accuracy", "precision", "f1", "recall"], cv=5)
metricas_rf = cross_validate(clasificador_rf, X, y, scoring=["accuracy", "precision", "f1", "recall"], cv=5)


# c) Calcular y comparar las métricas score, accuracy, precision, recall y F1 para ambos clasificadores

# Métricas Regresión Logística
accuracy_rl = metricas_rl["test_accuracy"].mean()
precision_rl = metricas_rl["test_precision"].mean()
recall_rl = metricas_rl["test_recall"].mean()
f1_rl = metricas_rl["test_f1"].mean()

# Métricas Random Forest
accuracy_rf = metricas_rf["test_accuracy"].mean()
precision_rf = metricas_rf["test_precision"].mean()
recall_rf = metricas_rf["test_recall"].mean()
f1_rf = metricas_rf["test_f1"].mean()

print("MÉTRICAS REGRESIÓN LOGÍSTICA")
print("Accuracy:", accuracy_rl)
print("Precision:", precision_rl)
print("Recall:", recall_rl)
print("F1:", f1_rl)

print("MÉTRICAS RANDOM FOREST")
print("Accuracy:", accuracy_rf)
print("Precision:", precision_rf)
print("Recall:", recall_rf)
print("F1:", f1_rf)

'''
Ambos clasificadores se comportan de manera similar, realizando buenas predicciones.
'''
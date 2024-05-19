from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Crear un modelo de árbol de decisión a partir del dataset wine disponible en la librería sklearn.
# (a) Utilizar el 65 % de los datos para entrenamiento y el 35 % restante para testeo.
wine = load_wine()

x = wine.data
y = wine.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.35, random_state=23
)

model = DecisionTreeClassifier(random_state=23)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# (b) Obtener las métricas Accuracy, Precision, Recall y F1
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred, average="micro"))
print("Recall:", metrics.recall_score(y_test, y_pred, average="micro"))
print("F1:", metrics.f1_score(y_test, y_pred, average="micro"))

# (c) Dar conclusiones sobre el modelo a partir de las métricas obtenidas.
"""

"""

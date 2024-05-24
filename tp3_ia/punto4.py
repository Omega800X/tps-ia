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
    x, y, test_size=0.35, random_state=1
)

model = DecisionTreeClassifier(random_state=1)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# (b) Obtener las métricas Accuracy, Precision, Recall y F1
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred, average="micro"))
print("Recall:", metrics.recall_score(y_test, y_pred, average="micro"))
print("F1:", metrics.f1_score(y_test, y_pred, average="micro"))

# (c) Dar conclusiones sobre el modelo a partir de las métricas obtenidas.
"""
Probando con algunos valores de random_state pude ver que las métricas tomaban
valores superiores al 0.8 y variando entre distintos valores debido a que el
clasificador es un árbol de decisión al cuál no se le aplicó ningún tuneo por
lo que presenta una alta varianza y un bajo sesgo.
Además probando con el valor del random_state=1 obtuve los siguientes valores para
las métricas:
Accuracy: 0.9206349206349206
Precision: 0.9206349206349206
Recall: 0.9206349206349206
F1: 0.9206349206349206

De lo cuál se puede decir que para ese valor de random_state el modelo
- Tuvo un acierto (TP + TN) del ~92% en sus predicciones.
- Tuvo una cantidad de verdaderos positivos sobre los positivos predichos del ~92%
- Tuvo una cantidad de verdaderos positivos sobre los positivos reales del ~92%
- De los casos que predijo como positivos tuvo un ~8% de FP
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay

# Dataset Breast Cancer Utilizar el dataset de cáncer de mama disponible en sklearn para predecir la
# presencia de cáncer maligno utilizando regresión logística.
# (a) Utilizar el 20 % de los datos para testeo.

ds = load_breast_cancer()
x = ds.data
y = ds.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
model = LogisticRegression(random_state=1, max_iter=10000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


# (b) Evaluar el rendimiento del modelo utilizando las métricas Accuracy, Precision y Recall.
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

# (c) Obtener la matriz de confusión del modelo
disp = ConfusionMatrixDisplay.from_estimator(model, x_test, y_test)
print(disp.confusion_matrix)

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# a) Cargar un dataset desde un archivo CSV usando
# la función loadtxt de NumPy

features = np.loadtxt(
    "high_diamond_ranked_10min.csv", delimiter=",", skiprows=1, usecols=range(2, 40)
)

target = np.loadtxt(
    "high_diamond_ranked_10min.csv", delimiter=",", skiprows=1, usecols=1
)

print(10 * "-", "FEATURES", 10 * "-")
print(features)
print(10 * "-", "TARGET", 10 * "-")
print(target)


# b) Dividir el dataset en un conjunto de entrenamiento y un conjunto de prueba usando la función
# train_test_split de NumPy.

x_train, x_test, y_train, y_test = train_test_split(
    features, target, test_size=0.3, random_state=1
)

print(10 * "-", "X_TRAIN", 10 * "-")
print(x_train)
print(10 * "-", "X_TEST", 10 * "-")
print(x_test)
print(10 * "-", "Y_TRAIN", 10 * "-")
print(y_train)
print(10 * "-", "Y_TEST", 10 * "-")
print(y_test)


# c) Normalizar los datos en el conjunto de entrenamiento usando la función StandardScaler de Scikit-
# learn.
scaler = StandardScaler()
scaler_results = scaler.fit_transform(x_train, y_train)

print(10 * "-", "SCALER_RESULTS", 10 * "-")
print(scaler_results)

# d) Aplicar la misma normalización al conjunto de prueba usando la función transform del objeto
# StandardScaler.
scaler_results = scaler.fit_transform(x_test, y_test)

print(10 * "-", "SCALER_RESULTS", 10 * "-")
print(scaler_results)

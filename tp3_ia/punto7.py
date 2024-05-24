import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 7. Dataset articulos_ml.csv
# A partir del dataset articulos_ml.csv que se encuentra disponible en el campus y contiene diversas
# URLs a artículos sobre Machine Learning. Se debe construir un modelo de regresión lineal para predecir
# cuantas veces será compartido un artículo en redes sociales basándonos en la cantidad de palabras del
# artículo.
# (a) Mostrar las columnas disponibles en el dataset articulos_ml.csv.

df = pd.read_csv("articulos_ml.csv")

print(df.columns)

df = df.drop(columns=["Title", "url"])
print(df.columns)

# (b) Crear gráficos para visualizar la relación entre las variables del dataset.

sns.pairplot(df)
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()

# (c) Filtrar los artículos que tengan menos de 3500 palabras y una cantidad de compartidos menor a
# 80,000 para analizar un conjunto más específico de datos.

df_filtrado = df[df["Word count"] < 3500]
df_filtrado = df_filtrado[df_filtrado["# Shares"] < 80000]
print(df_filtrado.head())

# (d) Utilizar los datos filtrados para generar un modelo de regresión lineal y graficar la relación entre
# las palabras del artículo y la cantidad de veces que son compartidos.
x = df_filtrado[["Word count"]]
y = df_filtrado["# Shares"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


model = LinearRegression()
model.fit(x_train, y_train)

plt.scatter(x, y, color="blue")
plt.plot(x, model.predict(x), color="red")
plt.show()

# (e) Utilizar el modelo generado para predecir la cantidad de veces que serán compartidos artículos de
# 2000, 5000 y 10000 palabras.

predicciones = model.predict([[2000], [5000], [10000]])
print(predicciones)

# (f) Mostrar los coeficientes del modelo.

print("Coeficientes: \n", model.coef_)

# (g) Evaluar el modelo aplicando las métricas Error Cuadrático Medio y Coeficiente de Deter-
# minación (R2).

y_pred = model.predict(x_test)

print(f"Error Cuadrático Medio: {mean_squared_error(y_test, y_pred)}")
print(f"Coeficiente de Determinación (R2): {r2_score(y_test, y_pred)}")

import pandas as pd
from sklearn.linear_model import LogisticRegression

columns = ["ID","Sex","Edad","SalarioEstimado","Compra"]

dataset = pd.read_csv("ClientesEnLinea.csv", header=0, names=columns)

feature_cols = ["ID","Sex","Edad","SalarioEstimado"]

x = dataset[feature_cols]
y = dataset["Compra"]

model = LogisticRegression(random_state=1, max_iter=10000)

# Dataset ClientesEnLinea.csv
# Crear un modelo de Regresión Logística utilizando el dataset ClientesEnLinea.csv que cuenta con in-
# formación de clientes que compran o no ciertos productos en línea para ello contamos con información
# sobre el género, la edad y el salario estimado, clasificando a los clientes con 0 y 1 si no compró o si
# compró respectivamente.
# Utilizar como métrica comparativa el promedio de una validación cruzada K-fold con 5 folds para
# entrenamiento y testeo.
# (a) ¿Cómo se comporta el modelo si consideramos todos los predictores?
# (b) ¿Qué sucede cuando solo consideramos como predictores Sexo y Edad?


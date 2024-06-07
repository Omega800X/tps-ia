import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 3. Dataset: teleCust.csv
# El dataset contiene la base de clientes de un proveedor de telecomunicaciones segmentada por servicio,
# categorizando a los clientes en cuatro grupos. Si los datos demográficos se pueden usar para predecir
# la pertenencia de grupo, la compañía podría personalizar las ofertas. Este ejemplo hace foco en datos
# demográficos, sean región, edad, estado civil, para predecir patrones de uso. El campo objetivo llamado
# custcat, tiene cuatro valores posibles que corresponden a los cuatro grupos de clientes: 1-Servicio Básico
# 2- E-Servicio 3- Servicio Plus 4- Servicio Total Utilizar un clasificador K vecinos más cercanos para
# predecir el grupo de los casos desconocidos o de testeo.
# a) Construir un programa Python para resolver el ejercicio. De ser necesario utilizar sklearn.preprocessing.
# para preparar los datos.

df = pd.read_csv(
    "teleCust.csv",
    header=0,
    names=[
        "region",
        "tenure",
        "age",
        "marital",
        "address",
        "income",
        "ed",
        "employ",
        "retire",
        "gender",
        "reside",
        "custcat",
    ],
)
print(df.shape)

X = df.drop(columns="custcat")
y = df["custcat"]

sc = preprocessing.StandardScaler()

scaled_X = sc.fit_transform(X)

# b) Separar el dataset original en dos porciones correspondiente a entrenamiento y testeo. Tener en
# cuenta que debo usar los mismos datos para todos los clasificadores que deba hacer (ver Incs (d)).

X_train, X_test, y_train, y_test = train_test_split(
    scaled_X, y, test_size=0.3, random_state=5
)


# c) Construir el clasificador KNN con 7 vecinos más cercanos.

knn7_default = KNeighborsClassifier(n_neighbors=7, weights="uniform")
knn7_default.fit(X_train, y_train)

# d) Obtener una versión alternativa del clasificador que difieran en la forma de la importancia relativa
# de los vecinos conforme a la distancia.

knn7_alt = KNeighborsClassifier(n_neighbors=7, weights="distance")
knn7_alt.fit(X_train, y_train)

# e) Utilizar acurracy como métrica de comparación entre ambos clasificadores. ¿Cuál es más preciso?

y_pred_def = knn7_default.predict(X_test)
y_pred_alt = knn7_alt.predict(X_test)

accuracy_def = accuracy_score(y_test, y_pred_def)
accuracy_alt = accuracy_score(y_test, y_pred_alt)

print("Accuracy knn7 def:", accuracy_def)
print("Accuracy kkn7 alt:", accuracy_alt)

"""Ambos clasificadores presentan precisiones muy similares entre sí, 
incluso probando con distintos random_state para realizar los splits."""

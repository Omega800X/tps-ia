from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.svm import SVC
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Dataset: StudentsPerformance
# El dataset contiene datos que abordan el rendimiento de un grupo de alumnos de nivel secundario. Los
# atributos de los datos incluyen las calificaciones de los alumnos, características demográficas, sociales
# y relacionadas con el centro escolar, y se recogieron mediante informes escolares y cuestionarios. Se
# proporcionan dos conjuntos de datos relativos al rendimiento en dos asignaturas distintas: Matemáticas
# (student-mat.csv) y Lengua portuguesa (student-por.csv). Queremos clasificar a los estudiantes en
# tres categorías, bueno, regular y malo, según su rendimiento en el examen final (final_score).

# Pre-procesamiento
# a) Generar un único dataset. Utilizar concat de la librería Pandas.

df_mat = pd.read_csv("student-mat.csv")
df_port = pd.read_csv("student-por.csv")

df = pd.concat([df_mat, df_port])

# b) Generar una nueva variable categórica final_grade a partir de los valores de final_score que asigne
# bueno a valores entre 15-20, regular a valores entre 10-14 y malo para los valores entre 0-9.


def get_final_grade(final_score):
    if final_score in range(15, 21):
        return "bueno"
    elif final_score in range(10, 15):
        return "regular"
    elif final_score in range(0, 10):
        return "malo"


df["final_grade"] = df["final_score"].apply(get_final_grade)
print(df.head())

# c) Graficar el mapa de calor para ver relación entre variables.

text_columns = [
    "school",
    "sex",
    "address",
    "family_size",
    "parents_status",
    "mother_job",
    "father_job",
    "reason",
    "guardian",
    "school_support",
    "family_support",
    "paid_classes",
    "activities",
    "nursery",
    "desire_higher_edu",
    "internet",
    "romantic",
]

le = LabelEncoder()

for feature in text_columns:
    df[feature] = le.fit_transform(df[feature])

plt.figure(figsize=(10, 10))
sns.heatmap(df.drop(columns="final_grade").corr(), annot=True)
plt.show()

# d) Analizar las características para ver si tienen una influencia significativa en el rendimiento final de
# los estudiantes.
"""
Las features que tienen una influencia significativa para el final score de los estudiantes son los scores de los períodos 1 y 2 y
en menor medida los fracasos (failures).
"""

# Modelos
# a) Utilizar labelEncoder para la variable final_grade
df["final_grade"] = le.fit_transform(df["final_grade"])
print(df.head())

# b) De ser necesario aplicar la función get_dummies.
# c) Dividir el dataset en entrenamiento y testeo, dejando el 30 % de los datos para testeo.

X = df.drop(columns="final_grade")
y = df["final_grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# d) Crear un modelo Random Forest para predecir el rendimiento académico de los estudiantes en
# función de diferentes características.

model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

precision_score_rf = precision_score(y_test, y_pred_rf, average="micro")

# e) Crear un modelo SVM.

model_svm = SVC(random_state=42)
model_svm.fit(X_train, y_train)
y_pred_svm = model_svm.predict(X_test)

precision_score_svm = precision_score(y_test, y_pred_svm, average="micro")

# f) Comparar el rendimiento de los modelos basándose en la precisión.
print("Precision Random Forest Classifier:", precision_score_rf)
print("Precision Support Vector Machine Classifier:", precision_score_svm)

"""El rendimiento del Random Forest Classifier fue mejor que el del model SVM."""

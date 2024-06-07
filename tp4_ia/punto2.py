import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# 2. Dataset: StudentsPerformance
# El dataset contiene datos que abordan el rendimiento de un grupo de alumnos de nivel secundario. Los
# atributos de los datos incluyen las calificaciones de los alumnos, características demográficas, sociales
# y relacionadas con el centro escolar, y se recogieron mediante informes escolares y cuestionarios. Se
# proporcionan dos conjuntos de datos relativos al rendimiento en dos asignaturas distintas: Matemáticas
# (student-mat.csv) y Lengua portuguesa (student-por.csv). Queremos clasificar a los estudiantes en
# tres categorías, bueno, regular y malo, según su rendimiento en el examen final (final_score).

col_names = [
    "school",
    "sex",
    "age",
    "address",
    "family_size",
    "parents_status",
    "mother_education",
    "father_education",
    "mother_job",
    "father_job",
    "reason",
    "guardian",
    "commute_time",
    "study_time",
    "failures",
    "school_support",
    "family_support",
    "paid_classes",
    "activities",
    "nursery",
    "desire_higher_edu",
    "internet",
    "romantic",
    "family_quality",
    "free_time",
    "go_out",
    "weekday_alcohol_usage",
    "weekend_alcohol_usage",
    "health",
    "absences",
    "period1_score",
    "period2_score",
    "final_score",
]


ds_mat = pd.read_csv("student-mat.csv", header=0, names=col_names)
ds_por = pd.read_csv("student-por.csv", header=0, names=col_names)


# Pre-procesamiento
# a) Generar un único dataset. Utilizar concat de la librería Pandas.
ds = pd.concat([ds_mat, ds_por], axis=0)
print(ds.shape)

# b) Generar una nueva variable categórica final_grade a partir de los valores de final_score que asigne
# bueno a valores entre 15-20, regular a valores entre 10-14 y malo para los valores entre 0-9.


def get_final_grade(final_score):
    if final_score in range(15, 21):
        return "bueno"
    elif final_score in range(10, 15):
        return "regular"
    elif final_score in range(0, 10):
        return "malo"
    else:
        return None


ds["final_grade"] = ds["final_score"].apply(get_final_grade)

print(ds)

# c) Graficar el mapa de calor para ver relación entre variables.

ds_copia = ds.copy(deep=True)


le = LabelEncoder()
text_columns = [
    "sex",
    "school_support",
    "family_support",
    "paid_classes",
    "activities",
    "nursery",
    "desire_higher_edu",
    "internet",
    "romantic",
    "final_grade",
    "school",
    "address",
    "family_size",
    "parents_status",
    "mother_job",
    "father_job",
    "reason",
    "guardian",
]

for attribute in text_columns:
    ds_copia[attribute] = le.fit_transform(ds_copia[attribute])

print(ds_copia.shape)

matriz_corr = ds_copia.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(matriz_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de calor")
plt.show()

# d) Analizar las características para ver si tienen una influencia significativa en el rendimiento final de
# los estudiantes.

"""
Los únicos predictores que tienen una influencia significativa en el rendimiento final de los estudiantes
son las calificaciones de los períodos 1 y 2, el resto de características no parecen afectar.
"""

# Modelos
# a) Utilizar labelEncoder para la variable final_grade
# b) De ser necesario aplicar la función get_dummies.

le = LabelEncoder()
ds["final_grade"] = le.fit_transform(ds["final_grade"])
print(ds.head())

ds = ds.drop(
    columns=[
        "school",
        "sex",
        "age",
        "address",
        "family_size",
        "parents_status",
        "mother_education",
        "father_education",
        "mother_job",
        "father_job",
        "reason",
        "guardian",
        "commute_time",
        "study_time",
        "failures",
        "school_support",
        "family_support",
        "paid_classes",
        "activities",
        "nursery",
        "desire_higher_edu",
        "internet",
        "romantic",
        "family_quality",
        "free_time",
        "go_out",
        "weekday_alcohol_usage",
        "weekend_alcohol_usage",
        "health",
        "absences",
    ]
)

# c) Dividir el dataset en entrenamiento y testeo, dejando el 30 % de los datos para testeo.
# d) Crear un modelo Random Forest para predecir el rendimiento académico de los estudiantes en
# función de diferentes características.
# e) Crear un modelo SVM.
# f) Comparar el rendimiento de los modelos basándose en la precisión.

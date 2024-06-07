from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# 4. Dataset: Wine Este dataset contiene información sobre las características químicas de diferentes vinos
# provenientes de tres diferentes cultivares en la región italiana de Piamonte. El objetivo es clasificar los
# vinos en tres categorías distintas basadas en estas características químicas.

# a) Realizar gráficos que permitan visualizar la relación entre las variables del dataset.
X, _ = load_wine(return_X_y=True, as_frame=True)

sns.pairplot(X)
plt.show()
sns.heatmap(X.corr(), annot=True)
plt.show()


# b) Obtener la curva Elbow para determinar la cantidad de clusters. Adjuntar imagen.

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
clusters_range = range(1, 51)

sse = []
for k in clusters_range:
    kmeans = KMeans(n_clusters=k, random_state=100)
    kmeans.fit(scaled_X)
    sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(clusters_range, sse)
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


# c) Construir el modelo K-means conforme a lo que indico en el punto anterior.

model = KMeans(n_clusters=20, random_state=100)
model.fit(scaled_X)
print(model.inertia_)

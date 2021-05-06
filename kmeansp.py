import math
import csv
import random

def distance(obj1, obj2, attributes):
    return math.sqrt(sum(
        [(obj1[attr] - obj2[attr]) ** 2 for attr in attributes]
    ))

def argmin(lista):
    return min(range(len(lista)), key=lambda x: lista[x])

# Entrada:
# 	k: Número de clústeres,
# 	D: Dataset compuesto de n objetos
def kmeans(k, D, attributes):            
# Método:
# 	1. Escoger k elementos de D como centros iniciales de los clústeres
    centroids = []
    new_centroids = [obj for obj in random.choices(D, k=k)]
    print(new_centroids)

# 	2. REPETIR
# 	3.	(re)asignar cada objeto al clúster, de acuerdo a la
#           "distancia" del objeto hacia el centro de cada clúster
    while [i for i in new_centroids if i not in centroids] != []:
        centroids = new_centroids
        clusters = []
        for _, obj in enumerate(D):
            cluster_index = argmin([distance(centroid, obj, attributes) for centroid in centroids])
            clusters.append(cluster_index)        
    # 	4.	actualiza el centro de cada clúster, en base a la nueva
    # 			composición del clúster
        new_centroids = [{}] * k
        sizes = [0] * k
        for i in range(len(D)):
            centroid, obj = new_centroids[clusters[i]], D[i]
            for attr in attributes:
                centroid[attr] = centroid.get(attr, 0) + obj[attr]
            sizes[clusters[i]] += 1
        for i in range(k):
            if sizes[i] == 0: continue
            for attr in attributes:
                new_centroids[i][attr] /= sizes[i]

        print("=====================")
        print(centroids)
        print(new_centroids)

# 	5. HASTA que se cumpla criterio de terminación
    return {}

if __name__ == "__main__":
    file = open("Mall_Customers.csv", newline='')
    dataset = []
    for row in csv.DictReader(file):
        nrow = {}
        for key, value in row.items():
            if key == "Genre":
                nrow[key] = value
            else:
                nrow[key] = float(value)
        dataset.append(nrow)
    kmeans(3, dataset, ["Annual_Income_(k$)", "Spending_Score"])

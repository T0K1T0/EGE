import random
from math import dist

k = 2 #изначально инициализируем количество кластеров
N = 10 # количество итераций в k - means
points = []

def preprocessing():
  with open('27A_18675.txt') as f:
    for point in f:
      point = point.replace(',', '.').split('	')
      points.append(list(map(float, point)))
  return points

def get_center(cluster):
  center = []
  for cl in cluster:
    min_sum = []
    for p in cl:
      sm = sum([dist(p, p1) for p1 in cl])
      min_sum.append([sm, p])
    center.append(min(min_sum, key=lambda x: x[0])[1])
  return center

def clusterization(points, center):
  cluster = [[] for _ in range(k)]
  for point in points:
    if dist(point, center[0]) < dist(point, center[1]):
      cluster[0].append(point)
    else:
      cluster[1].append(point)
  return cluster

def k_means(points):
  center = random.sample(points, k)
  for _ in range(N):
    cluster = clusterization(points, center)
    center = get_center(cluster)
  return center

points = preprocessing()
p1, p2 = k_means(points)

print((p1[0]+p2[0])/2*100000)
print((p1[1]+p2[1])/2*100000)
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


def draw(cluster):
    t = turtle.Turtle()
    turtle.screensize(3009, 3000)
    turtle.tracer(0)
    size = 120
    t.up()
    for points, color in zip(cluster, ('red', 'green', 'blue')):
        for point in points:
            t.goto(point[0]*size, point[1]*size)
            t.dot(6, color)
    turtle.done()


def mean_point(cluster):
    min_sum = []
    for p_1 in cluster:
        sm = sum(dist(p_1, p_2) for p_2 in cluster)
        min_sum.append([sm, p_1])
    return min(min_sum, key=lambda x: x[0])[1]


def dbscan(data):
    eps = 1
    df = data.copy()
    cluster = []
    while df:
        cluster.append([df.pop()])
        for p1 in cluster[-1]:
            points = [p for p in df if dist(p1, p) < eps]
            cluster[-1] += points
            for p in points:
                df.remove(p)
    return cluster


with open('27B_18675 (1).txt') as f:
    file = [nums.split() for nums in f]
    data = []
    for x, y in file:
        X = float(x.replace(',', '.'))
        Y = float(y.replace(',', '.'))
        data.append([X, Y])

    cluster = dbscan(data)
    point_2 = mean_point(cluster[0])
    point_1 = mean_point(cluster[1])
    point_3 = mean_point(cluster[2])

    res_1 = (point_1[0] + point_2[0]+point_3[0])/3 * 100000
    res_2 = (point_1[1] + point_2[1] + point_3[1])/3 * 100000

    print(res_1, res_2)
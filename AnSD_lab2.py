
import math
import copy
import random
import time


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
        
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * 
                     (p1.x - p2.x) +
                     (p1.y - p2.y) * 
                     (p1.y - p2.y)) 
  
def bruteForce(P, n):
    min_val = float('inf') 
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
  
    return min_val

def deltaMidleStripClosest(strip, size, d):

    min_val = d 

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - 
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
  
    return min_val 
  
def divideAndConcure(P, Q, n):

    if n==2:
        return dist(P[0], P[1])
    if n == 3: 
        return bruteForce(P, n) 
  
    mid = n // 2
    midPoint = P[mid]
  
    Pl = P[:mid]
    Pr = P[mid:]

    dl = divideAndConcure(Pl, Q, mid)
    dr = divideAndConcure(Pr, Q, n - mid) 
  
    d = min(dl, dr)

    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n): 
        if abs(lr[i].x - midPoint.x) < d: 
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d: 
            stripQ.append(Q[i])
  
    stripP.sort(key = lambda point: point.y)
    min_a = min(d, deltaMidleStripClosest(stripP, len(stripP), d)) 
    min_b = min(d, deltaMidleStripClosest(stripQ, len(stripQ), d))
      
      
    # distance is strip[] 
    return min(min_a,min_b)

def Merge(arr1, arr2, parameter):
    res = []
    cur1 = cur2 = 0
    while cur1 < len(arr1) and cur2 < len(arr2):
        if parameter == 'x':
            if arr1[cur1].x < arr2[cur2].x:
                res.append(arr1[cur1])
                cur1 += 1
            else:
                res.append(arr2[cur2])
                cur2 += 1
        if parameter == 'y':
            if arr1[cur1].y < arr2[cur2].y:
                res.append(arr1[cur1])
                cur1 += 1
            else:
                res.append(arr2[cur2])
                cur2 += 1
    if cur1 ==len(arr1):
        while cur2 < len(arr2):
            res.append(arr2[cur2])
            cur2 += 1
    if cur2 ==len(arr2):
        while cur1 < len(arr1):
            res.append(arr1[cur1])
            cur1 += 1
    return res

def MergeSort(arr, parameter):
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    a = arr[:half]
    b = arr[half:]
    return Merge(MergeSort(a, parameter), MergeSort(b, parameter), parameter)
  
def closest(P, n):
    MergeSort(P, 'x')
    Q = copy.deepcopy(P)
    MergeSort(Q, 'y') 
    return divideAndConcure(P, Q, n)
  
# Driver code
P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1), 
     Point(12, 10), Point(3, 4)]
n = len(P) 
print("The smallest distance is", closest(P, n))

with open("plot.txt", "w") as file:
    random.seed()
    for size in range(100, 10000, 100):
        points = []
        for i in range(size):
            points.append(Point(random.random() * size, random.random() * size))
        start = time.process_time_ns()
        clos = closest(points, size)
        t = time.process_time_ns() - start
        string = str(size)+ "; " + str(t)
        file.write(string + '\n')
        print('Size ' + str(size) + " done")
print("done")
  
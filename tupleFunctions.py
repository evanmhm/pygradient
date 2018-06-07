import math

def addTuples(x,y):
     z = []
     for i in range(len(x)):
         z.append(x[i]+y[i])
     return tuple(z)

def subTuples(x,y):
     z = []
     for i in range(len(x)):
         z.append(x[i]-y[i])
     return tuple(z)

def divTuple(x,y):
     z = []
     for i in range(len(x)):
         z.append(x[i]/y)
     return tuple(z)

def roundTuple(x):
    z = []
    for i in range(len(x)):
        z.append(int(math.floor(x[i] + 0.5)))
    return tuple(z)
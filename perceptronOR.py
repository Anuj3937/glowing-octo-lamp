import numpy as np
def activationFunction(v):
    if v>0:
        return 1
    else:
        return 0
def perceptronModel(x,w,b):
    v=np.dot(x,w)+b
    y=activationFunction(v)
    return y
def logicOR(x):
    w=np.array([1,1])
    b=-0.5
    return perceptronModel(x,w,b)
test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])
print(f"and logic for 0 and 0 is {logicOR(test1)}")
print(f"and logic for 0 and 1 is {logicOR(test2)}")
print(f"and logic for 1 and 0 is {logicOR(test3)}")
print(f"and logic for 1 and 1 is {logicOR(test4)}")
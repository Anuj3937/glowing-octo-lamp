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
def logicImplementationANDgate(x):
    w=np.array([1,1])
    b=-1.5
    return perceptronModel(x,w,b)
test1=np.array([0,0])
test2=np.array([0,1])
test3=np.array([1,0])
test4=np.array([1,1])
print(f"and logic for 0 and 0 is {logicImplementationANDgate(test1)}")
print(f"and logic for 0 and 1 is {logicImplementationANDgate(test2)}")
print(f"and logic for 1 and 0 is {logicImplementationANDgate(test3)}")
print(f"and logic for 1 and 1 is {logicImplementationANDgate(test4)}")
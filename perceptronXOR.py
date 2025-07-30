import numpy as np
def unitStep(v):
    return 1 if v >= 0 else 0
def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y
def NOT_logicFunction(x):
    wNOT = np.array([-1])
    bNOT = 0.5
    return perceptronModel(np.array([x]), wNOT, bNOT)
def AND_logicFunction(x):
    w = np.array([1, 1])
    bAND = -1.5
    return perceptronModel(x, w, bAND)
def OR_logicFunction(x):
    w = np.array([1, 1])
    bOR = -0.5
    return perceptronModel(x, w, bOR)
def XOR_logicFunction(x):
    y1 = AND_logicFunction(x)
    y2 = OR_logicFunction(x)
    y3 = NOT_logicFunction(y1)
    final_x = np.array([y2, y3])
    finalOutput = AND_logicFunction(final_x)
    return finalOutput
test_cases = [
    (np.array([0, 1]), (0, 1)),
    (np.array([1, 1]), (1, 1)),
    (np.array([0, 0]), (0, 0)),
    (np.array([1, 0]), (1, 0))
]
for test, vals in test_cases:
    print("XOR({}, {}) = {}".format(vals[0], vals[1], XOR_logicFunction(test)))

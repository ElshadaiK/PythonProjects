import numpy as np
z = [1,2,3]
y = [[1,2,3], [4,5,6],[7,8,9]]
x = [[[1,2,3],[1,2,3],[1,2,3]],
     [[4,5,6],[4,5,6],[4,5,6]],
     [[7,8,9],[7,8,9],[7,8,9]]
    ]
x1 = np.array(x)
y1 = np.array(y)
z1 = np.array(z)
#print(x1, "\n"*2, y1, "\n"*2, z1)

#Square Matrix => row = column
#Zero Matrix => np.zeros(order or row, column)
#Identity matrix => diagonal matrices + square(requires only one parameter)
#Unity matrix => 1

myZero = np.zeros((3,3)) -1*5
print(myZero)

myUnity = np.ones((3,4))
print(myUnity)

myIdentity = np.eye(4)
print(myIdentity)









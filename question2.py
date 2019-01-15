
import numpy as np 

a = np.random.randint(1000,size=(5,4)) 
print(a)

rows = a.shape[0]
cols = a.shape[1]

for i in range(0, rows):
    for j in range(0, cols):
        if (a[i,j]>50):
        	a[i,j]=100

print(a)

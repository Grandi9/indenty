import numpy as np 

a=np.random.randint(2, size=10)

print(a)

a[1::2]  = -10
print(a)

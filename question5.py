import numpy as np 

a=np.random.randint(2, size=10)

print(a)

N = 10

b=np.random.choice(a=[False, True], size=(N))  

print(b) 
result = a[b,...] 
print(result) 

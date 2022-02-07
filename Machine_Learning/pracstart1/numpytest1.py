import numpy as np
import tensorflow as tf

print(tf.__version__)

lst=np.arange(2,20,2)
#lst2=np.linspace(2,25,15)
#lst3=np.logspace(2,25,15)
#mano=np.random.randint(2,10)
#print(mano)
#mais=np.random.rand(2,2,3)
#print(mais)

#lst4=np.ones((3,4),int)
#print(lst4.reshape((-1,2)))

lst5=np.array([[2,3,4],[5,6,7],[2,5,6],[5,6,7]],int)


print(lst5.size)
print(lst5.reshape((2,-1)))
#lst6=lst5.reshape((-1,1))
#lst7=lst5.reshape((1,-1))
#lst8=np.concatenate(lst6,lst7)
#print(lst6+lst7)
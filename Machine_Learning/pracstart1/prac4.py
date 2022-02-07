import numpy as np
import matplotlib.pyplot as plt

w=np.array([[1,0.5],[2,1]])
print("axis of w : ",w.ndim)
print("shape of w : ",w.shape)

inp=np.array([[1,2],[-1,2]])
print("axis of inp : ",inp.ndim)
print("shape of inp : ",inp.shape)

b=np.array([-2.0,0.5])
print("axes of b : ",b.ndim)
print("shape of b : ",b.shape)

# let's apply linear combination

z = np.dot(w,inp)+b
print("shape of z : ",z.shape)
print(z)

#let's apply non linear activation with relu

#output=np.maximum(0. , z)
#it compares with 0. but other value doesn't work
#print("shape of output : ",output.shape)
#print(output)

# let's visualise few commonly use activations
#function of activation is bring non-linearity

x=np.linspace(-10,10,100)
#z1=np.maximum(0. , x)
#plt.plot(x,z1)
#plt.xlabel("x")
#plt.ylabel("relu(x)")
print(x)
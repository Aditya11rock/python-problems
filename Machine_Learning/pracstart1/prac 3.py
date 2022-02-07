
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

#print(x_train.ndim)
#print(x_train.shape)
#print(x_train.dtype)
#print(y_train.ndim)
#print(y_train.shape)
#print(y_train.dtype)
#print(x_test.ndim)
#print(x_test.shape)
#print(x_test.dtype)
#print("//**")
#print(y_test.ndim)
#print(y_test.shape)
#print(y_test.dtype)
#tensor slicing getting particular element

def showimage(img):
    plt.imshow(img,cmap=plt.cm.binary)
    plt.show()

#x_1=x_train[15]
#print(x_1)
#showimage(x_1)

#x_2=x_train[18]
#showimage(x_2)

#x_slice=x_train[10:100]
#print(x_slice.ndim)
#print(x_slice.shape)
#x4=np.array([10,20,30,40])
#print(x4.ndim)
#print(x4.shape)
x5=x_train[20:40]
#for i in x5:
#print(showimage(i))
x2=x_train[3]
print(x2.ndim)
print(x2.shape)
#x3=x_train[20:40]
#print(x3.shape)
#print(x3.ndim)

x_slice=x_train[10:100,7:-7 ,7:-7 ]
#print(x_slice.ndim)
#print(x_slice.shape)
#print(x_test.shape)
#print(x_test.ndim)

x_10=x_test[10]

#showimage(x_10)

x_11=x_test[10:15]
#for i in x_11:
#    showimage(i)


#these are the batch data set of size 128
#x12=x_train[:128]
#print(x12.ndim)

"""
mutliline comment in string 
"""
#top right corner
#x_13=x_train[:3,14:,:14]#batch sclicing according to requierment
#print(x_13.ndim)
#print(x_13.shape)
#for i in x_13:
#    showimage(i)

x_14=x_train[:3,7:21,7:21]
for i in x_14:
    showimage(i)
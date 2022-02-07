import numpy as np
import matplotlib.pyplot as plt
import math

N=50 #no of division

H=50 #cam shaft displacement
Out=60
Dwell=45
Return=90
offset=0

first=90-offset
second=first+Out
third=second+Dwell
fourth=third+Return

h=H*0.5
A=[ ]
B=[ ]
A3=[ ]
B3=[ ]

Theta1=np.linspace(0,Out,N)
for x in np.linspace (270,90,N): 
    a1=np.sin(np.radians(x)) 
    a2=h*a1
    if a2<0:
        a=a2+h
        a3=a+H
    elif a2>=0:
        a=a2+h
        a3=a+H
    A.append(a)
    A3.append(a3)

Theta2=np.linspace(Out+Dwell,Out+Dwell+Return, N) 
for x in np.linspace (90,270,N): 
    b1= np.sin(np.radians(x))
    b2=h*b1
    if b2<0:
        b=b2+h
        b3=b+H
    elif b2>=0:
        b=b2+h
        b3=b+H
    B.append(b)
    B3.append(b3) 

#ascent area
cc1=A3*np.cos(np.radians (np. linspace(first, second,N))) 
cs1=A3*np.sin(np.radians (np. linspace(first, second, N)))

#dwell Area
cc2=2*H*np.cos(np.radians (np.linspace(second, third, N)))
cs2=2*H*np.sin(np.radians (np. linspace(second, third, N)))

#descent Area
cc3=B3*np.cos(np.radians (np.linspace (third, fourth,N)))
cs3=B3*np.sin(np.radians (np.linspace (third, fourth, N)))

#inbetween Area
cc4=H*np.cos(np.radians(np.linspace(fourth, 360, N)))
cs4=H*np.sin(np.radians (np.linspace(fourth, 360,N)))

cc5=H*np.cos(np.radians (np. linspace(0, first,N)))
cs5=H*np.sin(np.radians (np.linspace(0, first, N)))

cc6=10*np.cos(np.radians (np. linspace(0,360,N)))
cs6=10*np.sin(np.radians (np.linspace(0,360,N)))

fig=plt.subplots (figsize=(12, 5))
plt.grid(True) 
plt.xlabel('Theta')
plt.ylabel('Lift')
plt.xticks (np.arange(0, Out+Dwell+Return+10, step=10))
plt.yticks(np.arange(0, H+5, step=5))
plt.plot(Theta1, A, Theta2, B)

fig= plt.subplots(figsize=(12, 10))
plt.grid(True)
plt.plot(cc1,cs1,cc2,cs2,cc3,cs3,cc4,cs4,cc5,cs5,cc6,cs6,color='red')
plt.plot(cc6,cs6,color='blue')
plt.show()




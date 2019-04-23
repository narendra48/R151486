import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
wp=0.35*np.pi
ws=0.7*np.pi
t=0.1
apf=2*np.tan(wp/2)/t
asf=2*np.tan(ws/2)/t
e=mp.sqrt((delp**-2)-1)
w=np.arange(0.1,np,pi,0.1)
k=mp.sqrt(((dels**-2)-1)/((delp**-2)-1))
d=(asf/apf)
n=np.abs((np.arccosh(k)/np.arccosh(d)))
N=np.ceil(n)
k=(N/2)
j=mp.sqrt(-1)
k1=1/N
yn1=((np.sqrt(1+sqrt(1+(e**(-2))))+(e**(-1)))**(k1)
yn2=((np.sqrt(1+sqrt(1+(e**(-2))))+(e**(-1)))**(k1)
yn=0.5*(yn1-yn2)
cs=(np.cos((((2*k)-1)*np.pi)/(2*N)))**(2)
ck=yn**(2))+cs
bk=(1/(np.sin((((2*k)-1)*np.pi)/(2*N)))*yn
e1=(1/(np.sqrt(1+(e**(2)))))
w=np.arange(0,np,pi,0.01)
z=np.exp(j*w)
s=(2/t)*((1-z**(-1))/(1+z**(-1)))
y1=e1*(apf**(2))*ck
y2=((s**(2))+(bk*s*apf)+((apf**(2))*ck))
hs=y1/y2
plt.xlabel('-------------->frequency')
plt.ylabel('Magnitude|H(e**(jw)|')
plt.title('Low pass Filter')
plt.plot(w,np,abs(hs))

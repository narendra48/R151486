import numpy as np
import matplotlib.pyplot as plt
rxy=[]
x=np.array(input('enter seq1='))
y=np.array(input('enter seq2='))
l1=len(x)
l2=len(x)
for l in range(-7,7,1):
	s=0
	for n in range(0,l1,l):
		if(n+l>=0 and n+l<l1):
			s=s+x[n+l]*y[n]
		rxx=np.append(rxy,s)
print rxy
n=np.linspace(-7,6,14)
plt.figure(l)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("cross correlation")
plt.stem(n,rxy)

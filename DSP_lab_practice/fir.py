import numpy as np
import matplotlib.pyplot as plt
import cmath as mp
def dtft(X):
	j=mp.sqrt(-1)
	w=np.linspace(-3.14,3.14,1000)
	l=x.size
	X=np.zeros(len(w),dtype=complex)
	for i in range(1000):
		su=0
		for i in range(0,1,1):
			su=su+x[n]*np.exp(-j*w[i]*n)
		X[i]=su
	return X
n=np.arange(-17,17,1)
hd=(0.25)*np.sinc(0.25*n)

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:35:41 2017

@author: Jian
"""

from numpy.polynomial import polynomial as P
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyval


def get_a(z,u):
    
    N=z.shape[0]
    g=np.zeros((N,N),dtype=complex)
    
    for i in range(N):
        g[0][i]=u[i]

    for i in range(1,N):
        for j in range(i,N):
            g[i][j]= (g[i-1][i-1] - g[i-1][j]) /( (z[j]-z[i-1])*g[i-1][j]  )
        
    a=np.zeros(N,dtype=complex)
    
    for i in range(N):
        a[i]=g[i][i]
 
    return a


def get_A(z,a):
    N=z.shape[0]     
    left=np.array([0])
    middle=np.array([a[0]])
    
    for i in range(1,N):
        c1=np.array( [-a[i]*z[i-1], a[i]  ]  )
        cc=P.polymul(c1,left)
        right=P.polyadd(middle,cc)
        left=middle
        middle=right
        
    return right
    
def get_B(z,a):
    N=z.shape[0]     
    left=np.array([1])
    middle=np.array([1])
    
    for i in range(1,N):
        c1=np.array( [-a[i]*z[i-1], a[i]  ]  )
        cc=P.polymul(c1,left)
        right=P.polyadd(middle,cc)
        left=middle
        middle=right
        
    return right
    
    
    
import numpy.polynomial.polynomial as poly

def roots_A_B(z,u):
    a=get_a(z,u)
    A=get_A(z,a)
    B=get_B(z,a)
    r_A=poly.polyroots(A)
    r_B=poly.polyroots(B)
    plt.scatter(r_A.real,r_A.imag,s=80, facecolors='none', edgecolors='black')
    plt.scatter(r_B.real,r_B.imag,s=80, marker='*',color='r')
    plt.axhline(0, color='green')
    plt.axvline(0, color='green')
    plt.show()
    
    return r_A, r_B

    
    
def f(my_z,z,a):
    A=get_A(z,a)
    B=get_B(z,a)
    return polyval(my_z,A)/polyval(my_z,B)
    
    
def rotate(Cwi):
    w=np.array(range(Cwi.shape[0]))
    wi=w*1j
    a=get_a(wi,Cwi)

    Cwi=f(w,wi,a)
    return Cwi.imag
    
def rotateM(Cwim):
    
    result=np.zeros(Cwim.shape)
    
    for i in range(Cwim.shape[0]):
        result[i]=rotate(Cwim[i])
 
    return result
    
    
    
    
    
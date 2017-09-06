# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:57:11 2017

@author: jian
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:26:20 2017

@author: jian
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  6 03:59:06 2017

@author: jian
"""
import numpy as np
import matplotlib.pyplot as plt


with open("27_best.dat") as infile:
    for line in infile:
        ha=np.array([ float(x) for x in line.split('\t')[0:-1]   ]  )
        c=ha.reshape(32,64)




plt.contourf(c)
plt.show()

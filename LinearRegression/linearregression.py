# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 23:12:34 2016

@author: fraz
"""

import numpy, math
import matplotlib.pyplot as plt



data = numpy.loadtxt('../data/data_IM_fault.txt');
#data = numpy.loadtxt('../data/f.txt');
data = data[:, 0]

print len(data)

xp = numpy.linspace(0, 2500, 33334)

plt.plot(xp, data, '-')
plt.ylim(-20, 20)
plt.show()

print numpy.mean(data);
print numpy.median(data);
print numpy.sqrt(numpy.mean(numpy.square(data)));


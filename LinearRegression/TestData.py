# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 19:38:56 2016

@author: fraz
"""
import numpy as np
class TestData():
    data = [];

    def __init__(self, path):
        self.data = np.loadtxt(path);

    def getAllData(self):
        return self.data;
        
    def getTemperatureData(self):
        return self.data[:, 0];

    def getPressureData(self):
        return self.data[:, 1];

    def getAngleData(self):
        return self.data[:, 2];

    def getTimeData(self, start=0, stop=250):
        return np.linspace(start, stop, len(self.data));
        
        
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 23:12:34 2016

@author: fraz
"""

import numpy
import matplotlib.pyplot as plt
from TestData import *


noFaultTestData = TestData('../data/Measurements_NoFault.txt');
iMFaultTestData = TestData('../data/Measurements_EMFault.txt');




def movingaverage(interval, windowSize):
    window = numpy.ones(int(windowSize))/float(windowSize)
    return numpy.convolve(interval, window, 'same')
    
    
def analyzeTemperatureData(noFaultData, faultData):
    xp = noFaultData.getTimeData();
    
    fig = plt.figure();
    tempPlot = fig.add_subplot(211);
    plt.ylim(250, 350);
    tempPlot.plot(xp, faultData.getTemperatureData(), 'r.');
    tempPlot.plot(xp, noFaultData.getTemperatureData(), 'g.');
    fig.suptitle("Temperature");
    maPlot = fig.add_subplot(212);
    noFaultTempAvg = movingaverage(noFaultData.getTemperatureData(), 1000);
    faultTempAvg = movingaverage(faultData.getTemperatureData(), 1000);
    plt.ylim(250, 350);
    maPlot.plot(xp, faultTempAvg, 'r-');
    maPlot.plot(xp, noFaultTempAvg, 'g-');
    
    fig.savefig('./results/temperature.pdf', bbox_inches='tight')
    
    fig.show()

    
def analyzePressureData(noFaultData, faultData):
    xp = noFaultData.getTimeData();
    
    fig = plt.figure();
    fig.suptitle("Pressure");
    pressurePlot = fig.add_subplot(211);
    
    pressurePlot.plot(xp, faultData.getPressureData(), 'r.');
    pressurePlot.plot(xp, noFaultData.getPressureData(), 'g.');
    
    maPlot = fig.add_subplot(212);
    noFaultPressureAvg = movingaverage(noFaultData.getPressureData(), 1000);
    faultPressureAvg = movingaverage(faultData.getPressureData(), 1000);
    plt.ylim(-15000, 150000);
    maPlot.plot(xp, faultPressureAvg, 'r-');
    maPlot.plot(xp, noFaultPressureAvg, 'g-');
   
    fig.savefig('./results/pressure.pdf', bbox_inches='tight')
    
    fig.show()

analyzeTemperatureData(noFaultTestData, iMFaultTestData);
analyzePressureData(noFaultTestData, iMFaultTestData);
#
#print numpy.mean(data);
#print numpy.median(data);
#print numpy.sqrt(numpy.mean(numpy.square(data)));




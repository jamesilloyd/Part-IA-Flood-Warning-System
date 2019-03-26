#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:43:00 2018

@author: Marco
"""

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    #Shifted to reduce the rounding errors
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly



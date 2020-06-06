#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-darkgrid')
from scipy import stats
import os
from scipy.stats import invgamma
import math


# In[4]:


def generate_beta_dist():
    dist = np.random.beta(4, 4, size=1000000)
    return(dist)

def convert_to_minutes(start, end):
    beg_minutes = start * 60
    end_minutes = end * 60
    return beg_minutes, end_minutes

def f(minutes):
    a = minutes // 60
    b = minutes % 60
    return [a,b]


# In[16]:


class sample_time():
    def __init__(self, beg_time, end_time, distribution, order_per_day):
        self.beg_time = beg_time
        self.end_time = end_time
        
        self.daypart = end_time - beg_time
        
        self.distribution = distribution
        self.order_per_day = order_per_day
        
    def change_in_time(self):
        print (self.end_time - self.beg_time)
        
    def sample_distribution(self):
        return np.random.choice(self.distribution, size=self.order_per_day, replace=True)
    
    def create_order_times(self):
        order_times = self.sample_distribution()
        
        order_times = order_times * self.daypart
        
        return (order_times)
        
        #'{:02d}:{:02d}'.format(*divmod(minutes, 60))


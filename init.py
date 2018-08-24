# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:56:39 2018

@author: jmo
"""

import pandas as pd
import os
import sys
import numpy as np
import importlib

os.environ['homeDir'] = "C:/Users/cheuk/Desktop/Analysis/" # SY Server
os.environ['homeDir'] = "C:/Users/cheuk/Desktop/Jefferies/Analysis/" # J Personal
os.environ['homeDir'] = "/home/jmo/Analysis/" # Js Windows
os.environ['homeDir'] = "C:/Users/jmo/Desktop/Analysis/" # Js Windows

os.chdir(os.environ.get('homeDir')+"lib")
ml = importlib.import_module("machineLearning_v3")
ml = importlib.reload(ml)
from test1 import *

os.chdir(os.environ.get('homeDir'))

df = pd.read_csv("./data/XLF-mlDF-forecast.csv", index_col = 'date')


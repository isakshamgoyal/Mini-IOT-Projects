# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:26:22 2019

@author: Spikee
"""

import pandas as pd
import random as rd
hours =['less than 3 hours', '3-10 hours', '11-18 hours', 'more than 20 hours']
age = ['10-16', '17-29', '29-45', 'above 45' ]
score = [1,2,3,4,5]
genre=['Action', 'Suspense thriller', 'Comedy', 'Drama', 'Romcom', 'Sci-Fi', 'Historical', 'Horror']


movieNames = pd.read_csv('MovieNames.csv', header='infer')

columns=['movie_id','cast','crew']
movieNames.drop(columns, axis=1, inplace=True)

m=movieNames.sample(n=3)

h=rd.sample(hours)

a=rd.choice(age)

s=rd.choice(score)

n = rd.randint(2,6)
g = rd.choices(genre, k=rd.randint(2,6))
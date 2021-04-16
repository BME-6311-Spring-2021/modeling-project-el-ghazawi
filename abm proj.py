# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:29:40 2021

@author: kooky
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#%%
file = ("C:\\Users\\kooky\\Documents\\BME 6311\\whabm.csv")
data = pd.read_csv(file) 
#%%
nphil1 = np.zeros((len(data['1 count neutrophils']), 10))
mphage1 = np.zeros((len(data['1 count neutrophils']), 10))
bf1 = np.zeros((len(data['1 count biofilm']), 10))
#%%
nphil1[:,0] = data['1 count neutrophils']
nphil1[:,1] = data['2 count neutrophils']
nphil1[:,2] = data['3 count neutrophils']
nphil1[:,3] = data['4 count neutrophils']
nphil1[:,4] = data['5 count neutrophils']
nphil1[:,5] = data['6 count neutrophils']
nphil1[:,6] = data['7 count neutrophils']
nphil1[:,7] = data['8 count neutrophils']
nphil1[:,8] = data['9 count neutrophils']
nphil1[:,9] = data['10 count neutrophils']

mphage1[:,0] = data['1 count macrophages']
mphage1[:,1] = data['2 count macrophages']
mphage1[:,2] = data['3 count macrophages']
mphage1[:,3] = data['4 count macrophages']
mphage1[:,4] = data['5 count macrophages']
mphage1[:,5] = data['6 count macrophages']
mphage1[:,6] = data['7 count macrophages']
mphage1[:,7] = data['8 count macrophages']
mphage1[:,8] = data['9 count macrophages']
mphage1[:,9] = data['10 count macrophages']

bf1[:,0] = data['1 count biofilm']
bf1[:,1] = data['2 count biofilm']
bf1[:,2] = data['3 count biofilm']
bf1[:,3] = data['4 count biofilm']
bf1[:,4] = data['5 count biofilm']
bf1[:,5] = data['6 count biofilm']
bf1[:,6] = data['7 count biofilm']
bf1[:,7] = data['8 count biofilm']
bf1[:,8] = data['9 count biofilm']
bf1[:,9] = data['10 count biofilm']
#%%
nphil2 = np.zeros((len(data['11 count neutrophils']), 10))
mphage2 = np.zeros((len(data['11 count neutrophils']), 10))
bf2 = np.zeros((len(data['11 count biofilm']), 10))
#%%
nphil2[:,0] = data['11 count neutrophils']
nphil2[:,1] = data['12 count neutrophils']
nphil2[:,2] = data['13 count neutrophils']
nphil2[:,3] = data['14 count neutrophils']
nphil2[:,4] = data['15 count neutrophils']
nphil2[:,5] = data['16 count neutrophils']
nphil2[:,6] = data['17 count neutrophils']
nphil2[:,7] = data['18 count neutrophils']
nphil2[:,8] = data['19 count neutrophils']
nphil2[:,9] = data['20 count neutrophils']

mphage2[:,0] = data['11 count macrophages']
mphage2[:,1] = data['12 count macrophages']
mphage2[:,2] = data['13 count macrophages']
mphage2[:,3] = data['14 count macrophages']
mphage2[:,4] = data['15 count macrophages']
mphage2[:,5] = data['16 count macrophages']
mphage2[:,6] = data['17 count macrophages']
mphage2[:,7] = data['18 count macrophages']
mphage2[:,8] = data['19 count macrophages']
mphage2[:,9] = data['20 count macrophages']

bf2[:,0] = data['11 count biofilm']
bf2[:,1] = data['12 count biofilm']
bf2[:,2] = data['13 count biofilm']
bf2[:,3] = data['14 count biofilm']
bf2[:,4] = data['15 count biofilm']
bf2[:,5] = data['16 count biofilm']
bf2[:,6] = data['17 count biofilm']
bf2[:,7] = data['18 count biofilm']
bf2[:,8] = data['19 count biofilm']
bf2[:,9] = data['20 count biofilm']



#%%
nphil3 = np.zeros((len(data['21 count neutrophils']), 10))
mphage3 = np.zeros((len(data['21 count neutrophils']), 10))
bf3 = np.zeros((len(data['21 count biofilm']), 10))
#%%
nphil3[:,0] = data['21 count neutrophils']
nphil3[:,1] = data['22 count neutrophils']
nphil3[:,2] = data['23 count neutrophils']
nphil3[:,3] = data['24 count neutrophils']
nphil3[:,4] = data['25 count neutrophils']
nphil3[:,5] = data['26 count neutrophils']
nphil3[:,6] = data['27 count neutrophils']
nphil3[:,7] = data['28 count neutrophils']
nphil3[:,8] = data['29 count neutrophils']
nphil3[:,9] = data['30 count neutrophils']

mphage3[:,0] = data['21 count macrophages']
mphage3[:,1] = data['22 count macrophages']
mphage3[:,2] = data['23 count macrophages']
mphage3[:,3] = data['24 count macrophages']
mphage3[:,4] = data['25 count macrophages']
mphage3[:,5] = data['26 count macrophages']
mphage3[:,6] = data['27 count macrophages']
mphage3[:,7] = data['28 count macrophages']
mphage3[:,8] = data['29 count macrophages']
mphage3[:,9] = data['30 count macrophages']

bf3[:,0] = data['21 count biofilm']
bf3[:,1] = data['22 count biofilm']
bf3[:,2] = data['23 count biofilm']
bf3[:,3] = data['24 count biofilm']
bf3[:,4] = data['25 count biofilm']
bf3[:,5] = data['26 count biofilm']
bf3[:,6] = data['27 count biofilm']
bf3[:,7] = data['28 count biofilm']
bf3[:,8] = data['29 count biofilm']
bf3[:,9] = data['30 count biofilm']

#%%
t1np = nphil1.mean(axis = 1)
t1mp = mphage1.mean(axis=1)
t1bf = bf1.mean(axis=1)

t2np = nphil2.mean(axis = 1)
t2mp = mphage2.mean(axis=1)
t2bf = bf2.mean(axis=1)

t3np = nphil3.mean(axis = 1)
t3mp = mphage3.mean(axis=1)
t3bf = bf3.mean(axis=1)

#%%
x = np.linspace(0, 7, 169)
fig, ax = plt.subplots()
ax.plot(x, t1np, '-b', marker='.')
ax.plot(x, t2np, 'r', marker='o')
ax.plot(x, t3np, marker='s')
ax.legend(['Bacteria Only', 'Biofilm: 5 initial microbes', 'Biofilm: 10 initial microbes'])
ax.set_title('Neutrophil Count over 1 Week')
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Count');
#%%
x = np.linspace(0, 7, 169)
fig, ax = plt.subplots()
ax.plot(x, t1mp, '-b', marker='.')
ax.plot(x, t2mp, 'r', marker='o')
ax.plot(x, t3mp, marker='s')
ax.legend(['Bacteria Only', 'Biofilm: 5 initial microbes', 'Biofilm: 10 initial microbes'])
ax.set_title('Macrophage Count over 1 Week')
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Count');
#%%
x = np.linspace(0, 7, 169)
fig, ax = plt.subplots()
ax.plot(x, t1bf, '-b', marker='.')
ax.plot(x, t2bf, 'r', marker='o')
ax.plot(x, t3bf, marker='s')
ax.legend(['Bacteria Only', 'Biofilm: 5 initial microbes', 'Biofilm: 10 initial microbes'])
ax.set_title('Biofilm Count over 1 Week')
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Count');
#%%
stats.ttest_ind(t2np, t1np)

#%%
tm1 = np.array(np.where(t1mp>100))[0,0] / 24
tm1f = np.array(np.where(t1mp>100))[0,-1] / 24
tm2 = np.array(np.where(t2mp>100))[0,0] / 24
tm2f = np.array(np.where(t2mp>100))[0,-1] / 24
tm3 = np.array(np.where(t3mp>100))[0,0] / 24
tm3f = np.array(np.where(t3mp>100))[0,-1] / 24

tn1 = np.array(np.where(t1np>100))[0,0] / 24
tn1f = np.array(np.where(t1np>100))[0,-1] / 24
tn2 = np.array(np.where(t2np>100))[0,0] / 24
tn2f = np.array(np.where(t2np>100))[0,-1] / 24
tn3 = np.array(np.where(t3np>100))[0,0] / 24
tn3f = np.array(np.where(t3np>100))[0,-1] / 24

tb1 = np.array(np.where(t1bf>100))[0,0] / 24
tb1f = np.array(np.where(t1bf>100))[0,-1] / 24
tb2 = np.array(np.where(t2bf>100))[0,0] / 24
tb2f = np.array(np.where(t2bf>100))[0,-1] / 24
tb3 = np.array(np.where(t3bf>100))[0,0] / 24
tb3f = np.array(np.where(t3bf>100))[0,-1] / 24

#np.where(t2mp>100)
#np.where(t3mp>100)
#Get the index value for when 100 count is
#reached and when it is under that
#arbitrary threshold












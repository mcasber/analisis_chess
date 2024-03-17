import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import random

df = pd.read_csv('C:\\Users\\Mariano\\Desktop\\Chess\\chess.csv',sep=",",header=0,
                 names = ['ranking', 'nombre', 'elo', 'norma', 'pais', 'juegos', 'nacido','continente'])

print(df.head()) 

year=2024
df['Edad']=df['nacido'].apply(lambda x : year - x)

df=df.fillna('euro')

#markers={1:'D', 2: 's'}
#sns.set(style='whitegrid', palette='dark', font="Verdana", font_scale=0.75)
#sns.countplot(data= df, y = 'pais') #sumar este
#sns.catplot(data= df, y = 'pais') # o este
'''
sns.jointplot(
    data= df, 
    x = 'elo',
    y = 'pais',
    marginal_ticks=True
    )
plt.show()'''

print(df)

print(df.groupby('continente').count())

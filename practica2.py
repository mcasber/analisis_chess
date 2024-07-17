import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Mariano\\Desktop\\Chess\\chess.csv',sep=",",header=0,
                 names = ['ranking', 'nombre', 'elo', 'norma', 'pais', 'juegos', 'nacido','continente'])

df['Edad']=df['nacido'].apply(lambda x : 2024 - x)

menores = df['Edad'] < 23
df_menores = df[menores]

#print(df.index) #RangeIndex(start=0, stop=200, step=1)
#print(df.shape) #(200, 9)
print(df)
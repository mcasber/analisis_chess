import pandas as pd
import numpy as np 

df1 = pd.read_csv('C:\\Users\\Mariano\\Desktop\\Chess\\chess.csv',sep=",",header=0,
                 names = ['ranking', 'nombre', 'elo', 'norma', 'pais', 'juegos', 'nacido','continente'])

df2 = pd.read_csv('C:\\Users\\Mariano\\Desktop\\Chess\\chess2.csv',sep=",",header=0,
                 names = ['ranking', 'jugador', 'elo', 'norma', 'pais', 'juegos', 'nacido','continente','ingresos'])

df3 = df1.merge(df2,left_on = 'nombre', right_on='jugador') #, how='left')

print(df3) 


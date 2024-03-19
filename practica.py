import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Mariano\\Desktop\\Chess\\chess.csv',sep=",",header=0,
                 names = ['ranking', 'nombre', 'elo', 'norma', 'pais', 'juegos', 'nacido','continente'])

print(df.head()) 
#print(df.info())

#   ranking             nombre   elo norma            pais  juegos  nacido
#0        1    Magnus Carlsen   2864    GM         Norway     3125    1990

#Nuevo registro
#new_row = [250, 'Marian', 2600, '1', 'Argentina', 3000, 1972]
# Insertar el nuevo registro en la ultima fila
#df.loc[200] = new_row
#print(df.tail(5))

#Condicionales
#indios= df[df['pais'].str.contains('India')]
#mayor_2700=df[df['elo']>2700]
#print(mayor_2700)

year=2024
df['Edad']=df['nacido'].apply(lambda x : year - x)

#print(df[df['Edad']>50])
#print(df.groupby('pais').max().reset_index())
#print(df.groupby('pais').agg(['min','max']))
#print(df.groupby('pais').agg({'elo':['min','max'],'juegos':'sum'}))

#markers={'Norway':'D', 'China': 's'}

sns.set(style='dark', palette='dark', font="Verdana", font_scale=0.75)
sns.relplot(
    data= df, 
    x = 'nacido', 
    y = 'elo',
    hue='pais'
    )
plt.show() 

#df.loc[0,['elo']]=3000

#df['Columna'] = 'fide'
#print(df.head(3))

#df['elo'] = df['elo'].astype(int)
#print(df.info())

# Análisis de Datos sobre los 200 jugadores top de ajedrez según el indicador elo fide.
Este notebook realiza un análisis exploratorio de datos de ajedrez y aplica el algoritmo K-means para agrupar jugadores con características similares.

## Técnicas Aplicadas:
1. **Análisis Exploratorio de Datos (EDA):** Se utilizan estadísticas descriptivas y visualizaciones para comprender la distribución de las variables, como 'elo' y 'age'.
2. **Preprocesamiento de Datos:** Se aplica `MinMaxScaler` para escalar las variables a un rango similar, lo cual es importante para el algoritmo K-means.
3. **Clustering con K-means:** Se utiliza el algoritmo K-means para agrupar a los jugadores en clusters basados en su 'elo' y 'age'.
4. **Método del Codo:** Se utiliza este método para determinar el número óptimo de clusters (*k*) para el algoritmo K-means.
5. **Visualización de Clusters:** Se crean gráficos de dispersión para visualizar los clusters y comprender la distribución de los jugadores en cada grupo.
6. **Análisis de Clusters:** Se calculan estadísticas descriptivas para cada cluster, como la media de 'elo' y 'age', para obtener insights sobre las características de los jugadores en cada grupo.

## Datos:
El dataset utilizado contiene información sobre los 200 jugadores top de ajedrez, incluyendo su 'rank', 'elo', 'games', 'birth_year' y 'age'.

## Resultados:
El objetivo de análisis es generar grupos de jugadores en base a la relación "age / elo"
Los resultados del clustering con K-means se visualizan y analizan para obtener insights sobre los diferentes grupos de jugadores.
import pandas as pd

#1. Creamos tu datos de transporte con contexto (Causas y Resultados)
datos = {
    'tiempo_real':[50, 95, 60,120, 45],
    'cliente': ['Walmart', 'Soriana', 'Oxxo', 'Walmart', 'Oxxo'],
    'clima': ['Despejado', 'Lluvia', 'Despejado', 'Niebla', 'Lluvia']
}

# 2. Convertimos el diccionario en una Tabla de Pandas (DataFrame)
df = pd.DataFrame(datos)

print("--- TODAS LA RUTAS REGISTRADAS ---")
print(df)

print("\n--- ALERTAS: FILTRANDO SOLO RETRASOS (> 60 min) ---")
# 3. La orden mágica de Paandas para filtrar
retrasos = df[df['tiempo_real']>60]

# 4. Agrega esta línea al final para ver el resultado en pantall.
print(retrasos)
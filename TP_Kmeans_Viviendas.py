import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ==========================================
# 1. Cargar los datos en un DataFrame
# ==========================================
datos = {
    'Jurisdiccion': [
        'CABA',
        'Buenos Aires',
        'Catamarca',
        'Chaco',
        'Chubut',
        'Córdoba',
        'Corrientes',
        'Entre Ríos',
        'Formosa',
        'Jujuy',
        'La Pampa',
        'La Rioja',
        'Mendoza',
        'Misiones',
        'Neuquén',
        'Río Negro',
        'Salta',
        'San Juan',
        'San Luis',
        'Santa Cruz',
        'Santa Fe',
        'Santiago del Estero',
        'Tierra del Fuego',
        'Tucumán',
    ],
    'Viviendas': [
        1391258,
        5970702,
        131978,
        368728,
        213317,
        1378237,
        370958,
        494473,
        194689,
        238141,
        140879,
        124149,
        639467,
        420101,
        254545,
        276371,
        404504,
        241436,
        182886,
        118047,
        1273460,
        311361,
        65535,
        493794,
    ],
}

df = pd.DataFrame(datos)

# Normalización previa necesaria para que el modelo trabaje equilibrado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Viviendas']])

# ==================================
# 2. Aplicar K-Means con 3 clusters
# ==================================
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# ==================================================
# 3. Asignar etiquetas interpretables a los clusters
# ==================================================
promedios_por_cluster = df.groupby('cluster')['Viviendas'].mean()
clusters_ordenados = promedios_por_cluster.sort_values().index

mapa_etiquetas = {
    clusters_ordenados[0]: 'Pocas viviendas',
    clusters_ordenados[1]: 'Cantidad media',
    clusters_ordenados[2]: 'Muchas viviendas',
}
df['etiqueta_grupo'] = df['cluster'].map(mapa_etiquetas)

# ====================================================
# 4. Mostrar a qué grupo pertenece cada jurisdicción
# ====================================================
print('--- ASIGNACIÓN DE JURISDICCIONES POR GRUPO ---')
print(df[['Jurisdiccion', 'Viviendas', 'etiqueta_grupo']].to_string(index=False))

# ============================================================
# 5. Visualizar los resultados en un gráfico de dispersión
# ============================================================
plt.figure(figsize=(13, 7))

colores_map = {
    'Pocas viviendas': 'blue',
    'Cantidad media': 'orange',
    'Muchas viviendas': 'red',
}

for etiqueta, color in colores_map.items():
  subset = df[df['etiqueta_grupo'] == etiqueta]
  plt.scatter(
      subset['Jurisdiccion'],
      subset['Viviendas'],
      color=color,
      label=etiqueta,
      s=90,
      edgecolors='black',
      linewidths=0.5,
  )

plt.xticks(rotation=45, ha='right', fontsize=10, fontweight='medium')

# Configuración del eje Y en millones
marcas_y = np.arange(0, 6_500_000, 500_000)


def formatear_millones(x, pos):
  if x == 0:
    return '0'
  return f'{x / 1_000_000:.1f} M'


plt.gca().yaxis.set_major_formatter(FuncFormatter(formatear_millones))
plt.yticks(marcas_y, fontsize=10)
plt.ylim(-200_000, 6_300_000)

plt.xlabel('Jurisdicción', fontsize=11, fontweight='bold')
plt.ylabel(
    'Viviendas Habitadas (Censo 2022 - En Millones)',
    fontsize=11,
    fontweight='bold',
)
plt.title(
    'Segmentación de Jurisdicciones Argentinas con K-Means (K=3)',
    fontsize=13,
    fontweight='bold',
    pad=15,
)

plt.legend(loc='upper left', fontsize=10, frameon=True)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
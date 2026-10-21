# 🎓 **Instituto Tecnológico Beltrán**

### 🤖 **Cátedra:** Procesamiento de Aprendizaje Automático

## **Trabajo Práctico: Segmentación de Viviendas con K-Means**
---
### 👩‍🏫 **Docente:** 
* Yanina Escudero

### 👥 **Integrantes del Grupo:**
* Danilo Figueroa
* María Alejandra Bernasconi Lahn
* Silvia Alejandra Gérez

# Segmentación de Viviendas en Argentina (INDEC 2022) 
*Un análisis práctico de Machine Learning usando K-Means y Python*

¡Hola! 👋 En este proyecto vamos a resolver un problema clásico de análisis de datos: **¿Cómo podemos agrupar a las 24 jurisdicciones de la Argentina según la cantidad de viviendas habitadas que tiene cada una?** 

Para lograrlo, aplicamos **K-Means**, un algoritmo de aprendizaje automático no supervisado, utilizando Python, Pandas, Scikit-Learn y Matplotlib. 

cómo funciona este código. 🧠✨

---

## 📌 ¿Cuáles son los pasos que sigue el programa?

El script está estructurado exactamente en **5 etapas lógicas**:

### 1️⃣ Cargar los datos en un DataFrame
* **¿Qué hacemos?** Creamos una tabla estructurada (un DataFrame de Pandas) donde volcamos las 24 jurisdicciones del país (usando abreviaturas limpias como *CABA*, *Buenos Aires*, etc.) junto con la cantidad exacta de viviendas registradas por el Censo INDEC 2022.
* **El detalle técnico:** Antes de pasar los datos al algoritmo, utilizamos una herramienta llamada `StandardScaler` para normalizar las escalas numéricas y asegurar que el modelo trabaje sobre una base matemática equilibrada.

### 2️⃣ Aplicar K-Means con 3 clusters (K=3)
* **¿Qué hacemos?** Le ordenamos al algoritmo de Inteligencia Artificial que analice las 24 provincias y las divida automáticamente en **3 grupos (`n_clusters=3`)** basándose en sus similitudes numéricas.
* **¿Cómo piensa el algoritmo?** K-Means calcula las distancias matemáticas entre los valores y junta en un mismo equipo a las provincias que tienen un parque habitacional parecido. Como resultado, nos devuelve etiquetas numéricas frías (por ejemplo, `0`, `1` y `2`).

### 3️⃣ Asignar etiquetas interpretables a los clusters
* **¿Qué problema resolvemos?** Los números `0`, `1` y `2` que nos da la computadora no nos dicen nada por sí solos. 
* **¿Cómo lo solucionamos?** Calculamos el promedio de viviendas de cada grupo para ordenarlos de menor a mayor y les ponemos nombres humanos que se entiendan a primera vista:
  * 🔵 **Pocas viviendas:** El bloque mayoritario de provincias con menor cantidad de hogares.
  * 🟠 **Cantidad media:** El grupo intermedio donde conviven distritos de gran peso demográfico (como CABA, Córdoba y Santa Fe).
  * 🔴 **Muchas viviendas:** El clúster superior integrado en absoluta soledad por la Provincia de Buenos Aires (el gigante demográfico del país).

### 4️⃣ Mostrar a qué grupo pertenece cada jurisdicción
* **¿Qué hacemos?** Imprimimos por consola una tabla limpia y ordenada para auditar los resultados. De este modo, podemos ver negro sobre blanco qué etiqueta le tocó exactamente a cada provincia según el criterio del modelo.

### 5️⃣ Visualizar los resultados en un gráfico de dispersión
* **¿Qué hacemos?** Traducimos todo el análisis matemático en una visualización profesional de alta calidad usando Matplotlib.
* **¿Qué mejoras le aplicamos para que se luzca?**
  * **Eje Y en Millones reales:** Estructuramos las marcas de la escala vertical de 500 mil en 500 mil (0, 0.5 M, 1.0 M... hasta 6.0 M) para reflejar con absoluta claridad la distancia real entre las provincias chicas, las medianas y el pico extremo de Buenos Aires.
  * **Eje X ordenado:** Rotamos y ajustamos los nombres cortos de las jurisdicciones para que respiren sin encimarse.
  * **Estética general:** Agregamos una paleta de colores contrastada, una leyenda flotante y una grilla de fondo 
---

### 🚀 ¿Cómo se ve esto en acción?
Al correr el script, tu consola te devolverá la clasificación completa provincia por provincia y se abrirá una ventana interactiva con el gráfico de dispersión listo para ser analizado, defendido o subido directamente a tu repositorio de GitHub. 

💻🔥

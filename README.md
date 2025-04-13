# 🛒 Análisis de Ventas por Tienda

Este proyecto analiza datos de ventas de **4 tiendas distintas**, con el fin de extraer estadísticas clave e identificar patrones relevantes en las operaciones comerciales.

## 📌 Propósito del análisis

El objetivo principal es obtener **métricas comparativas** entre distintas tiendas, tales como:

- Facturación total de cada tienda
- Categorías más populares
- Promedio de calificación de los clientes
- Productos más y menos vendidos
- Costo promedio de envío

Con estos datos, se busca ofrecer **insights** que ayuden a la toma de decisiones para optimizar ventas, logística y satisfacción del cliente.

---

## 🗂️ Estructura del proyecto

```
challenge1-data-science-latam/
├── 1.csv
├── 2.csv
├── 3.csv
├── 4.csv
├── analisis_ventas.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `1.csv` a `4.csv`: Archivos CSV con los datos de cada tienda.
- `analisis_ventas.py`: Script de Python que procesa los datos y muestra los resultados por tienda.
- `README.md`: Este archivo de documentación.

---

## 📊 Ejemplos de insights obtenidos

A continuación se muestran ejemplos típicos que genera el script:

```
📊 Resultados para Tienda 1:
- Facturación total: 1,150,880,400
- Categoría más popular: Muebles
- Calificación promedio: 3.98
- Producto más vendido: TV LED UD 4K
- Producto menos vendido: Auriculares con microfono
- Costo promedio de envío: 26018.61
```

```
🔍 --- Comparativa entre tiendas ---
🏆 La tienda con mayor facturación fue: Tienda 1 con 1,150,880,400
🌟 La tienda con mejor calificación promedio fue: Tienda 3 con 4.05
🚚 La tienda con el menor costo promedio de envío fue: Tienda 4 con 23459.46
```

> *(Opcional: podés agregar gráficos usando librerías como `matplotlib` o `seaborn` si lo deseás más adelante.)*

---

## 🚀 Instrucciones para ejecutar la app

### ✅ Requisitos

- Python 3.8 o superior
- Librería **pandas** instalada

### 💻 Pasos

1. Clonar o descargar el proyecto.
2. Asegurate de tener los archivos `1.csv`, `2.csv`, `3.csv` y `4.csv` en la misma carpeta que el script.
3. Ejecutar el script con:

```bash
python analisis_ventas.py
```

El script procesará los archivos, mostrará resultados por tienda y luego una comparativa general.

---

## 📬 Contacto

Para consultas o mejoras, podés escribirme directamente. ¡Tu feedback es bienvenido! 😊

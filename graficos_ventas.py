import json
import matplotlib.pyplot as plt

# Leer datos procesados
with open("resultados.json") as f:
    data = json.load(f)

# Ejemplo: Gráfico de barras de facturación total
# stores = list(data["ingresos"].keys())
# revenues = list(data["ingresos"].values())

# plt.figure(figsize=(8, 5))
# plt.bar(stores, revenues, color="skyblue")
# plt.title("Facturación total por tienda")
# plt.ylabel("Gs")
# plt.xlabel("Tiendas")
# plt.grid(axis="y", linestyle="--", alpha=0.6)
# plt.tight_layout()
# plt.show()

# Calificación promedio
# stores = list(data["calificaciones"].keys())
# ratings = list(data["calificaciones"].values())

# plt.figure(figsize=(8, 5))
# plt.bar(stores, ratings, color="orange")
# plt.title("Calificación promedio por tienda")
# plt.ylabel("Puntaje (0 a 5)")
# plt.ylim(0, 5)
# plt.grid(axis="y", linestyle="--", alpha=0.6)
# plt.tight_layout()
# plt.show()

# stores = list(data["envio_promedio"].keys())
# shipping = list(data["envio_promedio"].values())

# plt.figure(figsize=(8, 5))
# plt.bar(stores, shipping, color="green")
# plt.title("Costo promedio de envío por tienda")
# plt.ylabel("Gs")
# plt.grid(axis="y", linestyle="--", alpha=0.6)
# plt.tight_layout()
# plt.show()

# Conteo de categorías más populares por tienda
stores = list(data["categorias"].keys())
categories = list(data["categorias"].values())

plt.figure(figsize=(8, 5))
plt.bar(stores, categories, color="purple")
plt.title("Categoría más popular por tienda")
plt.ylabel("Categoría")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

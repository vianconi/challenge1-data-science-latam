import json
import pandas as pd

# Diccionarios para guardar los resultados por tienda
total_revenue_by_store = {}  # ingresos_totales_por_tienda
most_popular_category_by_store = {}  # categoria_mas_popular_por_tienda
average_rating_by_store = {}  # calificacion_promedio_por_tienda
most_sold_product_by_store = {}  # producto_mas_vendido_por_tienda
least_sold_product_by_store = {}  # producto_menos_vendido_por_tienda
average_shipping_cost_by_store = {}  # costo_promedio_envio_por_tienda

# Recorremos los archivos de las 4 tiendas
for store_number in range(1, 5):
    file_name = f"{store_number}.csv"

    try:
        df = pd.read_csv(file_name)

        store_key = f"Tienda {store_number}"

        # 1. Facturación total
        total_revenue = df["Precio"].sum()
        total_revenue_by_store[store_key] = total_revenue

        # 2. Categoría más popular (más veces repetida)
        most_popular_category = df["Categoría del Producto"].value_counts().idxmax()
        most_popular_category_by_store[store_key] = most_popular_category

        # 3. Promedio de calificación
        average_rating = df["Calificación"].mean()
        average_rating_by_store[store_key] = average_rating

        # 4. Producto más y menos vendido (frecuencia)
        product_counts = df["Producto"].value_counts()
        most_sold_product = product_counts.idxmax()
        least_sold_product = product_counts.idxmin()
        most_sold_product_by_store[store_key] = most_sold_product
        least_sold_product_by_store[store_key] = least_sold_product

        # 5. Costo promedio de envío
        average_shipping_cost = df["Costo de envío"].mean()
        average_shipping_cost_by_store[store_key] = average_shipping_cost

        # Mostramos los resultados por tienda
        print(f"\n📊 Resultados para {store_key}:")
        print(f"- Facturación total: {total_revenue:,.0f}")
        print(f"- Categoría más popular: {most_popular_category}")
        print(f"- Calificación promedio: {average_rating:.2f}")
        print(f"- Producto más vendido: {most_sold_product}")
        print(f"- Producto menos vendido: {least_sold_product}")
        print(f"- Costo promedio de envío: {average_shipping_cost:.2f}")

    except FileNotFoundError:
        print(f"⚠️ Archivo {file_name} no encontrado.")
    except Exception as error:
        print(f"❌ Error al procesar {file_name}: {error}")

# Comparativas entre tiendas
print("\n🔍 --- Comparativa entre tiendas ---")

# Tienda con mayor facturación
if total_revenue_by_store:
    top_revenue_store = max(total_revenue_by_store, key=total_revenue_by_store.get)
    print(f"🏆 La tienda con mayor facturación fue: {top_revenue_store} con {total_revenue_by_store[top_revenue_store]:,.0f}")

# Tienda con mejor calificación promedio
if average_rating_by_store:
    top_rating_store = max(average_rating_by_store, key=average_rating_by_store.get)
    print(f"🌟 La tienda con mejor calificación promedio fue: {top_rating_store} con {average_rating_by_store[top_rating_store]:.2f}")

# Tienda con menor costo promedio de envío
if average_shipping_cost_by_store:
    lowest_shipping_store = min(average_shipping_cost_by_store, key=average_shipping_cost_by_store.get)
    print(f"🚚 La tienda con el menor costo promedio de envío fue: {lowest_shipping_store} con {average_shipping_cost_by_store[lowest_shipping_store]:.2f}")


with open("resultados.json", "w") as f:
    json.dump({
        "ingresos": total_revenue_by_store,
        "categorias": most_popular_category_by_store,
        "calificaciones": average_rating_by_store,
        "producto_mas_vendido": most_sold_product_by_store,
        "producto_menos_vendido": least_sold_product_by_store,
        "envio_promedio": average_shipping_cost_by_store
    }, f, indent=4)

from dotenv import load_dotenv
import os
from woocommerce import API
#De esta forma llamo mi archivo Env.
load_dotenv()
cliente = os.getenv("cliente")
clave = os.getenv("secret")

wcapi = API(
    url="http://drevo.cl",
    consumer_key=cliente,
    consumer_secret=clave,
    version="wc/v3"
)
print('Buscando Productos')
#print(wcapi.get("products").json())
#print(wcapi.get("products/2812").json())
def buscarProducto(id):
    salida = wcapi.get(f"products/{id}").json()
    for valor in salida:
        if 'stock_quantity' in valor:
            print(salida[valor])

def updateProducto(id, valor):
    data = {
    "regular_price": valor,
    'stock_quantity': '20'
    }
    print('Actualizando precio')
    print(wcapi.put(f"products/{id}", data).json())

buscarProducto('2812')

updateProducto('2812','12345')

#buscarProducto('2812')
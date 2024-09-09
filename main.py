from dotenv import load_dotenv
import os
from woocommerce import API
import pandas as pd
#De esta forma llamo mi archivo Env.
load_dotenv()
cliente = os.getenv("cliente")
clave = os.getenv("secret")

#print(wcapi.get("products").json())
#print(wcapi.get("products/2812").json())



class wooComerceApi:
    def __init__(self):
        self.wcapi = API(
            url="http://drevo.cl",
            consumer_key=cliente,
            consumer_secret=clave,
            version="wc/v3"
        ) 

    def buscarProducto(self, id):
        salida = self.wcapi.get(f"products/{id}").json()
        for valor in salida:
            if 'stock_quantity' in valor:
                print(f"{valor} : {salida[valor]}")

    def updateProducto(self, id, valor, cantidad):
        print(f"Precio -> {valor}")
        data = {
        "regular_price": valor,
        'stock_quantity': cantidad
        }
        print('Actualizando precio')
        try:
            #print(self.wcapi.put(f"products/{id}", data).json())
            salida = self.wcapi.put(f"products/{id}", data).json()
            #print(salida['code'])
            if 'code' in salida:
                if salida['code'] == 'woocommerce_rest_product_invalid_id':
                    print("Id de Producto no valido")
                    return False
            return True    
        except:
            return False




df = pd.read_csv('product.csv')
producto = wooComerceApi()
print("Productos que se actualizaran")
print(df)
consulta = input("Desea continuar si/no: ")
if consulta == 'si':
    for i in range(len(df)):
        id = str(df.iloc[i]['id'])
        valor = str(df.iloc[i]['precio'])
        cantidad = str(df.iloc[i]['cantidad'])
        respuesta = producto.updateProducto(id,valor,cantidad)
        if respuesta:
            print(f'Producto id: {id} actualizado OK')
        else:
            print(f'Producto id: {id} no actualizo')
            
            
            






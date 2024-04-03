def leer_precios(cantidad):
    precios = []
    for i in range(0, cantidad):
        precio = float(input("Ingrese el precio del artículo " + str(i + 1) + ":"))
        precios.append(precio)
    return precios

def leer_ventas_sucursal(cantidad):
    ventas = []
    for i in range(0, cantidad):
        venta = float(input("Ingrese la cantidad vendida del artículo " + str(i + 1) + ":"))
        ventas.append(venta)
    return ventas


precios = leer_precios(5)
print("Precios:")
print(precios)

ventas_sucursales = []

for i in range(0, 4):
    print("Sucursal " + str(i + 1) + ":")
    ventas_sucursal = leer_ventas_sucursal(5)
    ventas_sucursales.append(ventas_sucursal)

print("Ventas por sucursal:")
for i in range(0, 4):
    print("Sucursal " + str(i + 1) + ":")
    print(ventas_sucursales[i])
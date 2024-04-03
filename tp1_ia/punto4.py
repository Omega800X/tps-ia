ventas = [[0 for _ in range(5)] for _ in range(4)]

precios = [0 for _ in range(5)]

for i in range(5):
    precios[i] = float(input(f"Introduce el precio del artículo {i+1}:"))

for i in range(4):
    for j in range(5):
        ventas[i][j] = float(
            input(
                f"Introduce la cantidad vendida del artículo {j + 1} en la sucursal {i + 1}: "
            )
        )

ventas_tot_articulos = [sum(ventas[i][j] for i in range(4)) for j in range(5)]

art_vendidos_sucursal2 = sum(ventas[1])

cant_art3_sucursal1 = ventas[0][2]

recaudacion_total_sucursales = [sum(ventas[i][j] * precios[j] for j in range(5)) for i in range(4)]

recaudacion_total_empresa = sum(recaudacion_total_sucursales)

sucursal_de_mayor_recaudacion = recaudacion_total_sucursales.index(max(recaudacion_total_sucursales)) + 1

print(f"Precios:\n{precios}")
print(f"Ventas por sucursal:\n{ventas}")
print(f"Totales vendidos por artículo:\n{ventas_tot_articulos}")
print(f"Cant. artículos vendidos sucursal 2:\n{art_vendidos_sucursal2}")
print(f"Cant. vendida del artículo 3 en la sucursal 1:\n{cant_art3_sucursal1}")
print(f"Recaudación total de cada sucursal:\n{recaudacion_total_sucursales}")
print(f"Recaudación total de la empresa:\n{recaudacion_total_empresa}")
print(f"La sucursal de mayor recaudación es la sucursal N°{sucursal_de_mayor_recaudacion}.")




productos = {"8475HD": ["Hp", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
             "fgdxFHD": ["Hp", 15.6, "12GB", "DD", "1T", "Intel Core i5", "integrada"],

             "2175HD": ["Acer", 14, "4GB", "SSD", "512GB", "Intel Core i7", "Nvidia GTX1050"],
             "123FHD": ["Acer", 14, "6GB", "DD", "1T", "AMD Ryzen 7", "integrada"],

             "342FHD": ["Lenovo", 17, "8GB", "SSD", "1T", "Intel Core i3", "Nvidia GTX1050"],
             
             "UWU1231HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 5", "Nvidia GTX1050"]}

stock = {"8475HD": [387990, 10], "fgdxFHD": [664990, 21],
         "2175HD": [327990, 4], "123FHD": [290890, 32],
         "342FHD": [444990, 7], "UWU1231HD": [349990, 1]}


def menu():
    global opcion
    opcion = input("""
*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Listado de productos.
4. Salir.

Ingrese opción: """)


def stock_marca(marca):
    cantidad = 0

    for valor_modelo, valor_marca in productos.items():
        if marca in valor_marca:
            cantidad += stock[valor_modelo][1]

    print(f"El stock es: {cantidad}")


def rango_precios():
    while True:
        try:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            break
        except ValueError:
            print("Debe ingresar valores enteros!!")
    
    busqueda_precio(p_min, p_max)


def busqueda_precio(p_min, p_max):
    notebooks_en_rango = []
    for valor_modelo, valor_stock in stock.items():

        if valor_stock[1] > 0:
            valor_precio = valor_stock[0]
            if p_min <= valor_precio <= p_max:

                marca = productos[valor_modelo][0]
                notebooks_en_rango.append(f"{marca}--{valor_modelo}")
    
    if any(notebooks_en_rango):
        notebooks_en_rango = sorted(notebooks_en_rango)
        print(f"Los notebooks entre los precios consultas son: {notebooks_en_rango}")
    else:
        print("No hay notebooks en ese rango de precios.")


def ordenar_productos():
    print("-------- Listado de Notebooks Ordenados --------")
    if any(productos):
        for valor_modelo, especificaciones in productos.items():
            print(f"{especificaciones[0]} - {valor_modelo} - {especificaciones[2]} - {especificaciones[4]}")
    else:
        print("No hay notebook disponibles para mostrar.")


while True:
    menu()
    if opcion == "1":
        marca = input("Ingrese marca a consultar: ").strip().title()
        stock_marca(marca)
    elif opcion == "2":
        rango_precios()
    elif opcion == "3":
        ordenar_productos()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opcion válida!!")
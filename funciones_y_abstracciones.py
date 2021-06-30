def busqueda_binaria():
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
        if respuesta**2 < objetivo :
            bajo = respuesta
        else:
            alto= respuesta

        respuesta = (alto + bajo) / 2

    print (f"la raiz cuadrada de {objetivo} es {respuesta}")

def enumeracion_exahustiva():
    respuesta = 0


    while respuesta**2 < objetivo:
        print (f"{objetivo}, {respuesta}")
        respuesta += .1

    if respuesta**2 == objetivo:
     print(f"la raiz cuadrada de  {objetivo} es {respuesta}")
    else:
        decimal = round(respuesta, 10)
        print (f"{decimal} es la raiz cuadrada de {objetivo}")




objetivo = int(input("Escoge un numero entero: "))
menu = """ "Metodo para encontrar la raiz:

1 - Metodo Binario
2 - Enumeracion matematica 

"""

opcion = int (input(menu))
if opcion ==1:
    busqueda_binaria()
elif opcion ==2:
    enumeracion_exahustiva()
else:
    print("Opcion no valida")
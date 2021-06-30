def run():
    nombre1 = input("¿Cual es tu nombre: ")
    edad1 = int(input("¿Cual es tu edad: "))
    nombre2 = input("¿Cual es el nombre de la segunda persona?: ")
    edad2 = int(input("¿Cual es la edad de la segunda persona: "))
    
    
    if edad1 > edad2:
        print (nombre1 + " Es mayor que " + nombre2 )
    elif edad2 > edad1:
        print(nombre2 + " Es mayor que " +  nombre1)
    else:
        print(nombre1 + " y " + nombre2 + " tienen la misma edad")


if __name__ == '__main__':
    run()
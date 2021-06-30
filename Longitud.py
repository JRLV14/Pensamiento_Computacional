def run():
    Nombre = input("Escribe tu nombre: ")
    Nombre = Nombre.replace (" ", "")
    letras = int(len (Nombre))
    print ("Hola " + Nombre + " Tu nombre tiene " + str(letras) + " letras")
 


if __name__ == '__main__':
    run()

#1) Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
#una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla.

#aquí creamos la lista, no contiene nada aún
lista_nombres = []
#un bucle for, porque ya que se necesita que sean 3 nombres, debe suceder 3 veces lo mismo.
for i in range(3):
    #se le pide al usuario que ingrese un nombre.
    nombre = (input("Ingrese nombre: "))
    #se escribe la lista con .append para que la variable nombre(osea el que ingreso el usuario) se guarde en la lista.
    lista_nombres.append(nombre)
#aquí se hace una variable para guardar el nombre mas largo. La función "len" se usa para medir la longitud de los nombres de la lista,
#luego "max" y en () el nombre de la lista para que así compare los nombres.
nombre_mas_largo = max(lista_nombres, key=len)
#y para terminar se imprimen los nombres que ingresó el usuario y el nombre más largo
print("Los nombres son: ", lista_nombres)
print("El nombre mas largo es: ", nombre_mas_largo)
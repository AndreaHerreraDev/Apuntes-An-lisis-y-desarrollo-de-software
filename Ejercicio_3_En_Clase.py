#Menu de impresion

print("Inserte 0 para ejecutar ejercicio bucles"),
print("Inserte 1 para ejecutar ejercicio lista nombre"),
print("Inserte 2 para ejecutar ejercicio fruta ejercicio"),
print("Inserte 3 para ejecutar ejercicio Tuplas/Inmutables"),
print("Inserte 4 para ejecutar ejercicio Aleatorio"),
print("Inserte 5 para ejecutar ejercicio Uso de in"),
print("Inserte 6 para ejecutar ejercicio Concatenar"),
print("Inserte 7 para ejecutar ejercicio tupla"),
print("Inserte 8 para ejecutar ejercicio LISTA VACIA"),
print("Inserte 9 para ejecutar ejercicio Inicio(Módulo1)"),
print("Inserte 10 para ejecutar ejercicio Nombre y fecha "),
print("Inserte 11 para ejecutar ejercicio Año y Día de la Semana"),
print("Inserte 12 para ejecutar ejercicio Min y Max "),
print("Inserte 13 para ejecutar ejercicio ABS"),
print("Inserte 14 para ejecutar ejercicio Potencia "),

ejercicio=int(input("Elija el ejercicio: "))

if ejercicio ==0:

    #POO Python
    #Bucles 
    count=0
    while(count<5):
        count=count+1
        print("Iteración número {}".format(count))
    else:
        print("bucle while finalizado")




elif ejercicio ==1:

    #POO-PYTHON ABC EJERCICIO
    NOMBRE=[]
    NOMBRE=['P','A','U','L','A']
    print(NOMBRE[0])






#recorre una lista

elif ejercicio ==2:

    #frutas ejercicio.

    frutas=['Manzana','Pera','Lulo','Mango','Banana']
    print(frutas)

    for FRUIT in frutas:
        print(FRUIT)


elif ejercicio ==3:
    #Tuplas/Listas inmutables.Es decir una vez declaradas

    valores=(1,2,3,4,5)

    #tuple with mixed datatypes
    valores_mixtos=(1, "Que tal?", 2.5, False)
    print(valores_mixtos) # Salida: (1, "Que tal?", 2.5, False)




#Ejercicio radom aleatorio #POOB
elif ejercicio==4:

    #Radon numeros aleatorios

    import random
    print(random.randrange(0, 30)) #hace un numero aleatorio desde ... hasta...




elif ejercicio ==5:

    #IN-> Es para una cadena de texto, si quiero sacar una palabra de un texto primero va (loque quiero sacar entre comillas liuego va el in )

    #EXTRAER VALORES DE UNA CADENA DE CARACTERES IN

    #EJEMPLO
    txt ="Ficha 3171608 Tercer Trimestre 2025!"
    print("Trimestre" in txt)




elif ejercicio ==6:

    #Concatenar valores/EJEMPLO 1

    a= "Ficha"
    b= "Aprendices"

    c=a+ " " + b
    print(c)


    #Concatenar valores/EJEMPLO 2

    age = 36
    txt = f"Mi nombre es sol y tengo {age}"
    print(txt)


elif ejercicio ==7:

    #EJERCICIO 8
    #TUPLA
    #Modificar el print

    YEAR=["2025","2026", "2027", "2028"]
    #Acceder a elementos

    print("Este_es_el_año",YEAR[0]) #muestra ""
    print("Este_es_el_año",YEAR[1]) #muestra ""
    print("Este_es_el_año",YEAR[2]) #muestra ""
    print("Este_es_el_año",YEAR[-1]) #muestra ""





elif ejercicio ==8:

    #Guardar datos en una lista
    #LISTA VACIA
    lista_vacia=[]

    #LISTA CON VALORES
    aprendices=["Andres","Carlos", "Juan", "Sol"]
    #Acceder a elementos

    print(aprendices[0]) #muestra "Andres"
    print(aprendices[1]) #muestra "Carlos"
    print(aprendices[2]) #muestra "Juan"
    print(aprendices[-1]) #muestra "Sol"




#TEMAS QUE DEBO SABER:(●'◡'●)
#VARIABLES, INPUT,OUTPUT(PRINT), +-*/ 








#fecha #MODULO 1
elif ejercicio ==9:
    import datetime
    x = datetime.datetime.now()
    print(x)


#NOMBRE Y FECHA 
elif ejercicio ==10: 

    import datetime
    x = datetime.datetime.now()
    print(x)


#EJERCICIO #1 /MODULO 1 (pendiente)

    a=("Mi nombre es: ")

    b=("Mi ficha es: ")

    C= a+ "Paula "  + b+ "3171608"
    print(C)


elif ejercicio ==11: 
#DEVUELVE EL AÑO Y EL NOMBRE DEL DIA DE LA SEMANA

    import datetime
    x = datetime.datetime.now()
    print(x.year) #(x.year,x.Day, x.month)
    print(x.strftime("%A"))# le da formato a la fecha 


elif ejercicio ==12:

 #The MIN() and MAX() funciones que se pueden usar
    x = min(5, 10, 25)
    y = max(5, 10, 25)

    print(x)
    print(y)

    z= prom(x, y)

    lista1=[3,4,5]
    print(lista1.min)
    print(lista1.max)
    print(lista1.count)


elif ejercicio ==13:

#QUE ES UN ABS 
#TIPO DE VARIABLE (ESTUDIAR)
int=input("INGRESE SU NOMBRE")
X= float(input("Ingrese numero"))
y= abs(X)
print(y)

elif ejercicio ==14:
#POTENCIA 4 ESTA ELEVADO A LA 4
x = pow(4, 3)
print(x)



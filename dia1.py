print(2+2)
print(5*5+2)
print(4*2+3/2)
print(4/3*4)
print("Hola Mundo")
print("Hola python!")
print("Hola "*100)#multiplica la cadena
print("2+2")#lee como texto
print(2+2)#suma de enteros concatenaciond e strings y ctrl s es para guardar 
a = 2*2#asignacion a la variable
print(a)
a=2
b=2
print(a+3)#, sirve para separar elementos
print("hola", 2, "Chau", 10)#esto hace que separe al imprimir 
print("hola", a, "chau")#imprimo mi variable separada por coma
#EJERCICIO
nombre= "Alexandra Maria"
edad= "22 anhos"
print("hola me llamo", nombre,  " y tengo", edad)#atender que y tenia que tener comillas tb o toma como variable no definida 
nombredos= "Eli"
print("hola",nombredos)
hobby="ninguno"
print("hola me llamo", nombre, "y tengo", edad, "anhos", "y mi hobby es", hobby)
#crear una lista datos que en el primer lugar este tu nombre y en el segundo este tu edad 
#imprimir "Hola me llamo ____, y tengo __ anhos"
datos=["Alexandra", "22"]
print('Hola me llamo', datos[0], 'y tengo', datos[1], "anhos" )
lista=["Alexandra", 2*2, "22", edad]
print(lista[1])#tambien puedo poner operaciones
print("Hola me llamo", lista[0], "me gusta el numero", lista[1], "y tengo", lista[3])
datos[0]="Alex"
print("hola me llamo", datos[0])
#append agrega siempre al final 
datos.append("Ingeniera Ambiental")
datos.append("ninguno")
print(datos)
datos.pop()
print(datos)#cuando voy a llamar una lista no le pongo comillas pq o sino me imprime el nombre como texto no el contenido
#funcion len() ==> lenght cuenta tb los espacios cada caracter cuenta
print(datos)
dimension_de_datos=len(datos)
print(dimension_de_datos)
#ejercicio obtener la dimension de la lista datos e imprimir
#"la lista datos tiene ...... elementos"
cantidad= len(datos)
print('La lista datos tiene', cantidad, " elementos")
print("La lista datos tiene", len(datos), "elementos")
#ejercicio. imprimir el ultimo elemento de una lista que no sabemos cuantos elementos tiene 
listados=[3,4,5,6,7,7]
print(listados)
print(len(listados))
print(len(listados)-1)
print(listados[5])
total=len(listados)-1
print(listados[total])
print(listados[len(listados)-1])
print(len(listados)/3)
print(listados[1], listados[3], listados[5])
#bucles/loops/ciclos/iteraciones ###
listas_temas=["variables", 'listas', 'tipo de datos']
#recorrer una lista e imprimir en cada ciclo 
#el valor del elemento con 3 signos de admiracion
#variables!!!
for alex in lista:
    print(alex,"!!!")
    print("Holi")
print("final")

for brother in listados:
    print(brother,"numeros enteros")
    print("que buen numero")
print("ahora cuenta los numeros")
for valor in range(1, 11):
    print('HOLA', valor)
    suma=valor
    #tarea: imprimir el resultado de la suma de llosnumeros del 1 al 10 usando range 
#for hola_mundo in range(1, 101):
   # print("Hola", hola_mundo)

#print(1+2+3+4+5+6+7+8+9+10)

listauno= [1+2+3+4+5+6+7+8+9+10]
a=0
for x in listauno:
   a=a+x
print (a)

variabless=0
for sumatorias in range(1,11):
   variabless=variabless + sumatorias
print(variabless)

def resta(numero1,numero2):
    return numero1-numero2
print(resta(20,2))

def division(numero1,numero2):
   return numero1/numero2
print(division(20,2))

def sumdev(num1,num2,num3):
   return num1+num2/num3
print(sumdev(10,2,6))#senecesita parentesis pq respeta orden prioridad

def sumdev2(num1,num2,num3):#esteacorde a este introducis cual queres que sea
   return (num1+num2)/num3#se debe de usar parentesis
print(sumdev2(10,2,6))

#tarea2
def saludo2(nombre,edad):
   print("Hola soy", nombre, "y tengo", edad, "anhos")
saludo2("Alex",22)
saludo2("Maria",23)


listauno= [1+2+3+4+5+6+7+8+9+10]
a=0
for x in listauno:
   a=a+x
print (a)

#crear una funcion suma_lista que reciba como argumento una lista 
#de numero y retorne la suma de sus elementos
#pistausar acumulador


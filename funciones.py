
def suma_lista(listita):#puede tener cualquier nombre y adentro debe coincidir
    a=0 #defino mi variable temporal
    for x in listita:
        a=a+x
        print(x) #esto debe estar dentro del para que no me retorne le ultimo sino todos
    return a

listita1= [1,2,3,4,5]
print (suma_lista(listita1))

def lista_cuadrado(listajeyma):
    a=[]
    for jeyma in listajeyma:
        a.append(jeyma*jeyma)
    return a
otralista = [1,4,9,16,25]
resultadocuadrado = lista_cuadrado(otralista) 
print(resultadocuadrado)


def lista_triple(listanueva):
    a=[]
    for numero in listanueva:
        a.append(numero*numero*numero)
    return a
listavieja = [1,2,3]
result = lista_triple(listavieja)
print(result)
##########################################
#eliminar todos los elementos de una lista utilizando for

grupo5=['Alex', 'F1', 'F2', 'F3']

print("antes", grupo5)
for J in grupo5:
    grupo5.pop()#sequedaalamitadmientras elimina el ultimo for recorre desde el primero
print("despues",grupo5)#forypopseencuentranenmedio

for J in range(len(grupo5)):#elimina pq conoce descubrelalongitud
    grupo5.pop()
print("despues", grupo5)
#remud remueve la primera existencia encontrada, hay que obtener el indice
#desafio crear una funcion suma_cuadrado que reciba una lista de
#numeros y retorne el valor de la suma de cada numero al cuadradro





#hiceunafuncionquetieneotrafuncion
listadoble= [1,2,3]
def suma_cuadradodos(listanueva):#le llamo a mi funcion anterior nomasya
    return suma_lista(lista_cuadrado(listanueva))
print(suma_cuadradodos(listadoble))


lista= ["Alex", "Steven", "Pedro", "Iris"]
def ausentes(listaparareprobar):
    for aus in listaparareprobar:
        print(aus)
ausentes(lista)

'''materialesbiometria=["balde", "Balanza", "regla"]
def registro("pescadoregistrado", biometria): #modificoaca para add text
    for pez in biometria:
        print(pez)'#modificar para add text
print(registro(materialesbiometria, "pescadoregistrado"))'''
##############################################################

ing_pan=["harina", "levadura", "sal", "azucar", "agua"] #defino mi lista de datos

def imprimir_lista(ingredientes, nombre_producto):
    print("lista de compras de", nombre_producto)#texto con 
    print("_______________________________")#paraseparar
    for producto in ingredientes:
        print(producto)#imprimecadaelementodelalista

imprimir_lista(ing_pan, "Pan")#mandapanarribacon ing_pan que es la listadecompras

ing_salsa = ["tomate", "azucar", "sal", "cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza")

#desafio probar
listadoble= [1,2,3]

'''def suma_cuadradodos(listanuevauno):
    a=[]
    for numero in listanuevauno:
        a= suma + a.append(numero*numero)
    return a
resultados= suma_cuadradodos(listadoble)
print(resultados)

def suma_cuadrado (n1,n2,n3):#falta que me sume estos 
    return n1+n2+n3
print(suma(resultados))'''
####################################3
#copiar luego
'''list_numeros=[1,2,3,4]
def suma_cuadrado(lista_n): #defino que parametro recibe funcion
    suma=0 #variable 0'''
##########CONDICIONALES###################
#if significa si
#else significa sino
'''== es igual 
>mayorque
<menorque'''
'''preguntas
if______: 
 procesos
else: 
procesos'''
####ejemplos
#el alumno aprobo o no 
a=70
if a > 60:#poner dos puntos si o si 
    print("Pasaste nde")
nota=43

if nota>=60:
    print("pasaste")
else: 
    print("nopasastehule")

#ejercicio creear una funcion que reciba como parametro
#unanotadel 1 al 100 e imprima 
#sipasaste o te aplazaste

nota1=61
nombre="Pepito"
def seraque(nota, nombre):
    if nota > 60: #sirequierecondicionpor eso al lado
        print("pasaste", nombre)
    else: #va abajo directo no condicion
        print("no pasaste", nombre)
        print("intenta de nuevo")

seraque(nota1, nombre)
####and y or#######
a = 7
if a > 5 and a < 10 and a != 7:
    print("a es mayor a 5 y menor a 10")
else: 
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")

def espacio(enter):
    print("                  ")

###no se puede comparar numero con strings
a=5
if a > 5 or a < 10:
    print("a es mayor a 5 y menor que 10")
else:
    print("ndera")
hola= "hola"#para meter un espacio 

espacio(hola)#para meter a espacio

edad = 5
if edad > 18:
    print("deberia estar en la facultad")
elif edad > 13:
    print("deberia de estar en el college")
elif edad > 6: 
    print("deberia estar en la escuela")
else:
    print("anda a tu house bbdlc")
espacio(hola)###print space
#Anidado
if edad > 18:
    print("Universidad")
else:
    if edad > 13:
        print("secundario")
    else:
        if edad > 6:
            print("primaria")
        else:
                print("bbdlc")
#ej crear una funcion puntaje que reciba como parametro 
#unanotadel 1 al 100 e imprima que nota sacaste
#nota < 60 -----> 1
#nota entre 60 y 70 ----> 2 
#nota entre 71 y 75 -----> 3
#nota entre 76 y 85 -----> 4
#nota entre 76 y 85 -----> 5
#nota mayor que 85 ---> 5
numero = 59
name="Alex"
def calificacion(a, nombre):
    
    if a < 60:
        print("calificacion 1", nombre)
    elif a >= 60 and a <= 70: 
        print("calificacion 2", nombre)
    elif a > 70 and a <=75: 
        print("calificacion 3", nombre)
    elif a > 75 and a <= 85: 
        print("calificacion 4", nombre)
    elif a > 85: 
        print("calificacion 5", nombre)
calificacion(numero, name)
calificacion(78, "WILLY")
calificacion(98, "aprobado")
espacio(hola)
#################################
#desponerquesalgaelnombredealguien
espacio(hola)
#ir probando y que entre en cada cosa
#hacer que retorne valores en vez de print
###INPUT
#definir funciones luegoconesto
#22 identifica la posicion en que posicion de gpio esta conectado, la patitas de la raspberry pi 
#alpresionaresuntrue, humedad va a ser una entrada, 
#cada vez que apretemos tenemos que haccer pasar a esto 
import RPi.GPIO as gpio
from time import sleep

led_r = 23
led_g = 24
led_y = 25
entrada = 22
gpio.setmode(gpio.BCM)
gpio.setup(led_r, gpio.OUT)
gpio.setup(led_g, gpio.OUT)
gpio.setup(led_y, gpio.OUT)
gpio.setup(entrada, gpio.IN)
contador = 0

while True:
	condicion = gpio.input(entrada)

print ("chauhola")











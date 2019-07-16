#Tipo de dato string/cadena/str de texto
"esto es un string"
#tipo de dato Integer/entero/int
105
[] #esto es una lista 
["Alexandra", 22, "Ingeniera Ambiental"] #lista de 3 elementos
#variables no permite coma, espacio, ni que sea un numero ni coma, name significativo
nombre= "Alex"
edad= 21+1
edad_mal= "22+2"
variablelista=["HOLA", nombre, 99]
#acceder a un elemento de la lista
print(variablelista[0], edad, variablelista[2])
#acciones/operaciones
variablelista.append("futbol") #add element list
variablelista.pop() #eliminar ultimo elemento
variablelista[2]="programador"
print(variablelista)
#imprimir un elemento de una lista
for bonita in variablelista: #variablelista si o si para que recorra
    print(bonita)
#imprimir los numeros del 1 al 10 
for cualquiercosa in range(10):
    print(cualquiercosa + 1)
 #imprimir el ultimo numero de la lista
 #solucion paso por paso
print(len(variablelista))
palabrafinallista=len(variablelista)-1
print(palabrafinallista)

#range de nuevo practica
for numero in range (1,10):
    print(numero)
#imprimir hola 10 veces 
for numero in [1,2,3,4,5]:
    print('hola', numero)



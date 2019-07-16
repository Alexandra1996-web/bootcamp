import RPi.GPIO as gpio #libreta para utilizar los puertos de 
from time import sleep #es para dar pausas 
led1=23 #definimos los pines de GPIO a utilizar
gpio.setmode(gpio.BCM)
#modo BCM de la raspberry pi (Broadcom SOC channel)
gpio.setmode(gpio.BCM)
#configuramos los puertos conectados a los leds como salida
gpio.setup(led1,gpio.OUT)#configuramos los puertos conecta

while True: #bucle infinito
    gpio.output(led1,True) #encendemos el led1
    sleep(1) #encendemos el led1
    gpio.output(led1, False) #apagamos el led1
    #pausa de un segundo
    sleep(1) 
#ejercicio 
#hacer que los tres leds parpaden todos juntos con un intervalo de 0.5 segundos
import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25

gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

while True:
	gpio.output(led_r,True)
	sleep(1)
	gpio.output(led_r,False)
	sleep(1)
	gpio.output(led_y,True)
	sleep(1)
	gpio.output(led_y,False)
	sleep(1)
	gpio.output(led_g,True)
	sleep(1)
	gpio.output(led_g,False)
	sleep(1)


import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25

gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

while True:
	gpio.output(led_r,True) #encender
	gpio.output(led_g,True)
	gpio.output(led_y,True)
	sleep(0.5)
	gpio.output(led_r,False) #apagar
	gpio.output(led_g,False)
	gpio.output(led_y,False)
	sleep(0.5)
#siempretenemosqueimportarlalibreriaetc
#out es pqsacamosenformacion leindicamos enque patitia es conectada
#sleep para que le de tiempo a la compy de procesar
import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25
gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

listaopen = [led_r, led_g, led_y]
	
while True:
	for x in listaopen:
		gpio.output(x, True)
		sleep(1)
		gpio.output(x, False)
		sleep(1)
import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25
gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

listaopen = [led_r, led_g, led_y]
tiempo = 0.2
	
while True:
	for x in listaopen:
		gpio.output(x, True)
		sleep(tiempo)
	for x in listaopen:
		gpio.output(x, False)
		sleep(tiempo)
import RPi.GPIO as gpio #libreria para puertos
from time import sleep #para dar pausas

led_r = 23
led_y = 24
led_g = 25
gpio.setmode(gpio.BCM)
gpio.setup(led_r,gpio.OUT)
gpio.setup(led_y,gpio.OUT)
gpio.setup(led_g,gpio.OUT)

listaopen = [led_r, led_g, led_y]
tiempo = 0.2
	
while True:
	for x in listaopen:
		gpio.output(x, True)
		sleep(tiempo)
	for x in listaopen:
		gpio.output(x, False)
		sleep(tiempo)
	"dddddddd"
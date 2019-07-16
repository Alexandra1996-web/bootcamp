import rodi#llamar a los archivos
import time

#crear objeto, p guardar acciones son metodos 
robot = rodi.RoDI()
#()llevan las aciones o metodos
#vamosatraerelmetodomoverydormir

'''robot.move_forward()
time.sleep(2)
robot.move_left()#izquierda
time.sleep(2)
robot.move_backward()#atras
time.sleep(2)
robot.move_stop()'''

'''robot.move_forward()#adelante
time.sleep(1)#tiempo
robot.move_right()#giraderecha
time.sleep(0.5)
robot.move_forward()
time.sleep(1)
robot.move_right()
time.sleep(0.5)
robot.move_forward()
time.sleep(1)
robot.move_right()
time.sleep(0.5)
robot.move_forward()
time.sleep(1)
robot.move_right()
time.sleep(0.5)
robot.move_forward()
time.sleep(1)'''


'''robot.move_forward()#adelante
time.sleep(1)#tiempo
robot.move_right()
time.sleep(0.5)
robot.move_forward()#adelante
time.sleep(1)#tiempo
robot.move_left()
time.sleep(0.5)
robot.move_forward()
robot.sleep(1)'''
'''robot.move_stop()'''

'''robot.move_left()#izquierda
time.sleep(0.5)
robot.move_forward()#adelante
time.sleep(1)#tiempo
robot.move_left()#giraizq
time.sleep(0.5)
'''
#robot.move_backward()#atras
#time.sleep(1)#tiempo

'''for x in range (1,5):
    robot.move_forward()#adelante
    time.sleep(1)#tiempo
    robot.move_right()#giraderecha
    time.sleep(0.5)
    robot.move_stop()

contador = 0 
while contador <=3:
    contador = contador + 1
    robot.move_forward()#adelante
    time.sleep(2)#tiempo
    robot.move_stop()
    robot.move_right()#giraderecha
    time.sleep(0.5)
    robot.move_stop()'''
#####sensor de distancia###
#ultrasonicoemiteyrecibeelrebotedeesesonidopodemosusareldedijgango
#ondasdesonidochocarebotayregresaluz
#ladistanciaencmaloquetienedentroimprimirsiquieroverlqtienedentro

#bucleinfinito
#ctrl c interrupcion por teclado
'''variable = 3

while variable == 3:#mientrasseatresvariableejecutaelblog
    
    print (robot.see(), "centimetros")'''
'''while True:
    print (robot.see(), "centimetros")
    robot.move_forward()'''

'''try:#intentaresto
    while True:
        print (robot.see(), "centimentros")#imprimimos la distancia
        robot.move_forward()
except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
    print("finalizado")
    robot.move_stop()''' #alapreta control c + c p robot


'''print (robot.see(), "centimetros")
robot.move_forward()
time.sleep(2)
robot.move_left()#izquierda
time.sleep(2)
robot.move_fackward()#atras
time.sleep(2)

robot.move_stop()
'''
#ejercicio utilizando un while True: bucle infinito
#hacer que RoDi avance si no encuentra un obstaculo enfrente
'''try:
    while True:
        print (robot.see(), "centimentros") #avanza 
            
        if robot.see() < 5: #mayora5pareeimprimepareypareelsensor
            print("pare")
            robot.move_stop()
        else:#paraqueavancesinodetectaalgo
            robot.move_forward() 
except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
    print("finalizado")
    robot.move_stop()#medafinalizadoyfinal
robot.move(50,50)'''

# try:
#     while True:

#         print (robot.see(), "centimentros") #avanza 
            
#         if robot.see() > 10: #mayora5pareeimprimepareypareelsensorsigue
#                 print("siga")
#                 robot.move_right() 
#                 robot.pixel(0,0,100)
#         else:#paraqueavancesinodetectaalgo
#                 robot.move_forward()
#                 robot.move(200,200)
#                 robot.pixel(0,100,0)
#                 robot.pixel(100,0,0)
#                 robot.pixel(0,100,0)
#                 robot.pixel(0,0,100)
#                 robot.sing(10000,5000)
#                 print(robot.light(),"lux")
#                 time.sleep(0.5)

# except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
#     print("finalizado")
#     robot.pixel(100,0,100)
#     robot.move_stop()#medafinalizadoyfinal
#     #sensor de linea, colores devuelve valores altoy oscuro  900 800 
#     #seguidor de luz

'''try:
    while True:
        print (robot.light(), "luxex") #valorluz
            
        if robot.light() > 10: #
            print("siga")
            robot.move_right() 
            robot.pixel(0,0,0)
        else:#paraqueavancesinodetectaalgo
            robot.move_forward()
            robot.move(200,200)
            robot.pixel(0,100,0)
            robot.pixel(100,0,0)
            robot.pixel(0,100,0)
            robot.pixel(0,0,100)
            robot.sing(100000,2000)
except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
    print("finalizado")
    robot.pixel(100,0,100)
    robot.move_stop()#medafinalizadoyfinal'''

'''while True:
    print(robot.light(), "lux")
    time.sleep(0.5)
try:
    #while True:
       # print (robot.see(), "centimentros") #avanza 
            
        #if robot.see() > 10: #mayora5pareeimprimepareypareelsensorsigue
          #  print("siga")
            robot.move_right() 
            robot.pixel(0,0,100)
        else:#paraqueavancesinodetectaalgo
            robot.move_forward()
            robot.move(200,200)
            robot.pixel(0,100,0)
            robot.pixel(100,0,0)
            robot.pixel(0,100,0)
            robot.pixel(0,0,100)
            robot.sing(100000,2000)
except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
    print("finalizado")
    robot.pixel(100,0,100)
    robot.move_stop()#medafinalizadoyfinal'''
    
'''try: #lux
    while True:
        print (robot.light(), "luxex") #valorluz
            
        if robot.light() > 10: #
            print("siga")
            robot.move_right() 
            robot.pixel(0,0,0)
        else:#paraqueavancesinodetectaalgo
            robot.move_forward()
            robot.move(200,200)
            robot.pixel(0,100,0)
            robot.pixel(100,0,0)
            robot.pixel(0,100,0)
            robot.pixel(0,0,100)
            robot.sing(100000,2000)

except KeyboardInterrupt: #excepto cuando hay una interrupcion por 
    print("finalizado")
    robot.pixel(100,0,100)
    robot.move_stop()#medafinalizadoyfinal'''
#seguidordelinea
while True:
    linea = robot.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    time.sleep(0.5)


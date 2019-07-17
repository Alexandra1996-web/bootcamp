class Dino:
    ojos = 2

    def __init__(self, un_nombre, un_color, canti_patas=4, un_genero=None):#metodoconstructivodefinoatributosdemiobjeto
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("Naci")
    def saludar(self, respuesta):#traelosatributos
        print("Hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", self.genero)
        print(respuesta)#add the argumentonuevp
    def cortar_pata(self, cantidad_patas_a_cortar=1): #ledejaspordefectoalgoquerestaropcionalvalor
        self.patas = self.patas - cantidad_patas_a_cortar #ledecisapatasquetomeesvalor
    def oper(self, cantidad_patas_a_multiplicar=2):
        self.operpata = self.patas * cantidad_patas_a_multiplicar 
        return self.operpata  #guardarelvalor
    def decir_genero(self):
        '''
        esto dice su genero, documento lo que dice asi abro esto
        '''
        print("Hola soy", self.nombre, "y me identifico como", self.genero)

pepitocreaobjeto = Dino ("Alex", "verde")
pepitocreaobjeto.saludar("holiiiis")#noolvidarsiesmetodoseponeparentesis y add argumento new
pepitocreaobjeto.decir_genero()
print(pepitocreaobjeto.oper())


#herencia toma una clase anterior para crearse
class Trex(Dino): #en la clase Trex hereda los emtodos y atributos definidos
    #en la clase Dino
    def __init__(self, nombre, patas=4, color=None):
        self.nombre = nombre
        self.patas = patas
        self.color = color 
        print("Hola soy un Trex y me llamo", self.nombre)
robert =  Trex("Roberto el Trex")
print(robert.ojos)
robert.saludar("hola grupo")

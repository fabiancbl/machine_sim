#COMENTAR TU CODIGO DESCRIVIENDO LAS FUNCIONES 

def asm_pio(*args, **kwargs):
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

# FUNCION 1.

''' asm_pio: Es esta funcion se tendran dos parametros de entrada los cuales son: args y kwargs, los cuales permiten pasar un número variable de argumentos a una
funcion, pero al especificar arg viene de argumentos y son parámetros de entrada de una función, en el caso de kwargs permite pasar argumentos
de longitud variable asociados con un nombre o key a una función, en esta funcion se define el DECORADOR, en el cual entra el programa, y posteriormente
se define el compilador en el cual se imprime el programa y retornan las funciones '''


def decorador_instr(fun_inst):
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

#FUNCION 2.

'''decorador_instr: Es una funcion decorador en la cual esta entrando la funcion fun_inst, dentro de la cual
esta un decorador de esa funcion de entrada con otros parametros de la funcion que entro al decorador, dentro de
la cual se llama al self que permite ejecutar las variables y las funciones, para posteriormente ser ejcutada y retornada'''


class PIO():
    OUT_LOW='PIO.OUT_LOW'

# como se define la clase
    
'''clase en la cual se definen los pines y su valor de entrada'''


class StateMachine:

'''clase dentro la cual tienen unas funciones'''
  def _init(self, id, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine._init',id, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass


'''_init_ es una funcion a la cual la cual tienen ciertos parametros de entradas, algunos definidos con un valor,
se definen dos varibles globales, que posteriormente son definidas como self, por lo tanto se sabe en que momento va a inicializar la funcion en el programa, 
posteriormente se crea una lista vacia, en la cual posteriormente se van a imprimir diferentes datos que son comparados e ingresados en el sistema'''
        
  def active(self, x=None):
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')
        '''definimos el esatdo de la variable x para un valor'''



fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def _init_(self,*args, **kwargs):
        global sm_iniciandose
        print(self._class.name)#,'nop.init_',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def _getitem_(self,name):
        #print('nop._getattr_',name)
        pass

'''clase decorador, en la cial se crea variable global, e inicia la lista de instrumentos, imprimiendo unos variables definidas'''       
 
class set(nop):
    def _init_(self,*args, **kwargs):
        super()._init_(*args, **kwargs)
        pass

  '''clase set en la cual se definen variables de entrada para un parametro, y hereda unos datos con la funcion super'''    
    
class wrap_target(nop):
    def _init_(self,*args, **kwargs):
         super()._init_(*args, **kwargs)
         pass 

  '''clase wrap, en la cial se definen variables de entrada para un parametro, y se heredan unos datos'''       

class wrap(nop):
    def _init_(self,*args, **kwargs):
         super()._init_(*args, **kwargs)
         pass 
         
      '''clase wrap, --> variables de entrada para un parametro, y se heredan unos datos''

class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data

    def __getitem__(self,i):
        print("Indice: ",i)
        if isinstance(i,slice):
            print("slice",i.start,i.stop,i.step)
            
    #Realizar lecturas según su posición

    def iloc(self,i):

        
        if isinstance(i,slice):
            print("hola")
        if isinstance (i,int):
                    print("entero")
                    titulos=self.data.keys()
                    for j in titulos:
                        valores=self.data[j]
                        print ("Titulo: ", j)
                        print("Dato solicitado: ",valores[i])
                        print("\n")

def read_csv(arch,sep=','):
    arch = open(arch)
    linea=arch.readline() #renglones
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        data[titulo]=[]
        titulos.append(titulo) #guarda titulos
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)

    
            
    
    
datos="hola.csv"       
d=read_csv(datos)
#d=DataFrame([1,'a','b','c',8,9,10])
#print(d.data)

try:
    d.iloc[5:8]
except:
    print("hola22")







#    A         B         C         D
#  0.469112, -0.282863, -1.509059, -1.135632
# 1.212112, -0.173215,  0.119209, -1.044236
# -0.861849, -2.104569, -0.494929,  1.071804
#  0.721555, -0.706771, -1.039575,  0.271860
# -0.424972,  0.567020,  0.276232, -1.087401
# -0.673690,  0.113648, -1.478427,  0.524988

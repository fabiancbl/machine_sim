class DataFrame:
    def __init__(self,data,*args,**kwargs):
        self.data=data
        
    def __getitem__(self, indice):
        print('indice',indice)
        if isinstance(indice,slice):
            print('slice',indice.start,indice.step,indice.stop)
    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices=[]
            indices.append(indice)
            return indices
            
            
def read_csv(arch,sep=';'):
    arch = open(arch)
    linea=arch.readline()
    data={}
    titulos=[]
    for titulo in linea.split(sep):
        titulo = titulo.strip()
        data[titulo]=[]
        titulos.append(titulo)
    for linea in arch.readlines():
        for i,elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem.strip())
    return DataFrame(data)
            
        
#prueba
d=read_csv('datos.csv')
print(d.data)
#listilla=DataFrame._index_('datos.csv')

#print(d[2])
#print(d[3:9:2])
#print(d[:])

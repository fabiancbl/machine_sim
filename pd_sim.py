import numpy as np


class DataFrame:
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __getitem__(self, indice):
        print('indice', indice)
        if isinstance(indice, slice):
            print('slice', indice.start, indice.step, indice.stop)

    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

    def T(self, d):
        # print("Hola Mundo"
        print(d.data)
        keys = dict.keys(d.data)

    # Realizar lecturas según su posición
    def iloc(self, i):
        # if isinstance (i,slice):
        #   if isinstance (j,slice):

        if isinstance(i, int):
            titulos = self.data.keys()
            # for i in range(0,i):
            # print(self.data[i])
            #   a=d.data[i][0];

    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices

    def _setitem_(indice, valor):
        pass


def funcion_tail(arch, n):
    with open(arch) as f:
        lineas = [lineas.strip('\n') for lineas in f.readlines()]
    return lineas[-n:]


def read_csv(arch, sep=';'):
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __getitem__(self, indice):
        print('indice', indice)
        if isinstance(indice, slice):
            print('slice', indice.start, indice.step, indice.stop)


def funcion_crea_Archivo(arch, sep=','):
    # esta funcion creara y guardara un nuevo archivo CSV con el mismo contenido.
    pass


def funcion_tail(arch, n, sep=';'):
    with open(arch) as f:
        lineas = [lineas.strip('\n') for lineas in f.readlines()]
    return lineas[-n:]


def funcion_tail(arch, n, sep=';'):
    with open(arch) as f:
        lineas = [lineas.strip('\n') for lineas in f.readlines()]
    return lineas[-n:]


def read_csv(arch, sep=','):
    arch = open(arch)
    linea = arch.readline()
    data = {}
    titulos = []
    for titulo in linea.split(sep):
        titulo = titulo.strip()
        data[titulo] = []
        titulos.append(titulo)
    for linea in arch.readlines():
        for i, elem in enumerate(linea.split(sep)):
            data[titulos[i]].append(elem)
    return DataFrame(data)


# prueba
d = read_csv('datos.csv')
print(d[6])
print(d[3:9:2])
print(d[:])

# x=sum(map(len,d.data.values()))
# print(x)


for t in d.data:
    print(t, ":", d.data[t])


print("\n", funcion_tail("datos.csv", 5))


# pruebaaa
d = read_csv('datos.csv')
print(d.data)

# prueba Willian
# d=read_csv('datos.csv')
# print(d.data)
z = len(funcion_tail("datos.csv", 5))

print("\n", funcion_tail("datos.csv", 5))

strA = "".join(funcion_tail("datos.csv", 5))

print(strA)


# Nicolas Arevalo 20202005024
# Crear el comando copy
def copy(arch, sep=';'):
    arch = open(arch)


# prueba
d = read_csv('datos.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])


# prueba
d = read_csv('datos.csv')
print(d.data)


# Función para seleccionar por etiquetas (loc), identificar filas y columnas identificando si es un str, int, slice.
def loc(columna, fila=None):
    pass
    # dat = titulo
    # fila = titulo


# prueba
# prueba
d = read_csv('datos.csv')
print(d.data)
print(d[6])
print(d[3:9:2])
print(d[:])
# print(d.data)
# print(d[2])
# print(d[3:9:2])
# print(d[:])
# listilla=DataFrame._index_('datos.csv')

# print(d[2])
# print(d[3:9:2])
# print(d[:])


# prueba
d = read_csv('datos.csv')
print(d.data)
for c in d.data.keys():
    print(d.data[c])

for t in d.data:
    print(t, ":", d.data[t])


print("\n", funcion_tail("datos.csv", 5))


# pruebaaa
d = read_csv('datos.csv')
print(d.data)

for t in d.data:
    print(t, ":", d.data[t])


print("\n", funcion_tail("datos.csv", 5))


# pruebaaa
d = read_csv('datos.csv')
print(d.data)

# prueba Willian
# d=read_csv('datos.csv')
# print(d.data)

# creando el metodo que pide como parametro un diccionario
# y le agrega un index en las filas


# dic{} = {'A': 1, 'B': 2, 'C': 3}

# key, value = 'D', 4
# def rowIndex(dic{})


# dictionary.update({key: value})
# print(dictionary)
# d1 = {
#   "Nombre": "Sara",
#   "Edad": 27,
#   "Documento": 1003882
# }

# df=pd.DataFrame()
# nombres = ['Juan', 'Laura', 'Pepe']
# edades = [42, 40, 37]
# df['Nombre'] = nombres
# df['Edad'] = edades
# print(df)

# prueba

d = read_csv('datos.csv')
d.T(d)


d = read_csv("datos.csv")
# d=DataFrame([1,'a','b','c',8,9,10])
print(d.data)
d.iloc(5)


#                   A         B         C         D
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
# *2013-01-04  0.721555 -0.706771 -1.039575  0.271860
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401
# 2013-01-06 -0.673690  0.113648 -1.478427  0.524988

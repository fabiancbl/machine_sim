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

    def iloc(self, i, j):
        # if intance(i, j):
        #     for i in range(0,i):
        pass

    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices


def __getitem__(self, i):
    print("Indice: ", i)


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


def read_csv(arch, sep=';'):
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
            data[titulos[i]].append(elem.strip())
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

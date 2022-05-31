import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

puntoSol = []

# ecuaciones e intervalos (para tabular)
# rango de la grafica .arange
x = np.arange(-10,100,20)
y = np.arange(-10,100,20)
#yMin = (-120*x)/200
y1 = 65-x
y2 = 20+0*x
y3 = (3000-60*x)/24
x1 = 23+(0*y)

#Identificadores para las lineas
primerLinea = LineString(np.column_stack((x,y1)))
segundaLinea = LineString(np.column_stack((x,y2)))
tercerLinea = LineString(np.column_stack((x,y3)))
#cuartaLinea = LineString(np.column_stack((x,yMin)))
quintaLinea = LineString(np.column_stack((x1,y)))

#Se grafican las lineas
plt.plot(x, y1, '-', color='b')
plt.plot(x, y2, '-', color='g')
plt.plot(x, y3, '-', color='r')
#plt.plot(x, yMin, '-', color='y')
plt.plot(x1, y, '-', color='k')

#configuraciones adicionales del grafico
plt.grid()
plt.xlabel('Cursos de administracion')
plt.ylabel('Cursos ajenos al area de administracion')
plt.title('Metodo Grafico')

#buscando los puntos de interseccion
primerInter = primerLinea.intersection(quintaLinea)
segundaInter = tercerLinea.intersection(primerLinea)
tercerInter = quintaLinea.intersection(tercerLinea)

#Graficar los vertices
plt.plot(*primerInter.xy, 'o')
plt.plot(*segundaInter.xy, 'o')
plt.plot(*tercerInter.xy, 'o')

#Imprimiendo las coordenadas de los vértices en la consola
print('\n COORDENADAS DE LAS INTERSECCIONES')
print('Coordenadas de la primera intersección: {} '.format(primerInter))
print('Coordenadas de la segunda intersección: {} '.format(segundaInter))
print('Coordenadas de la tercer intersección: {} '.format(tercerInter))

#identificando los valores de las coordenadas x,y de cada vertice
x1in, y1in = primerInter.xy
x2in, y2in = segundaInter.xy
x3in, y3in = tercerInter.xy


#Cambiar el formato de matriz a float
x1i = np.float(np.array(x1in))
x2i = np.float(np.array(x2in))
x3i = np.float(np.array(x3in))
y1i = np.float(np.array(y1in))
y2i = np.float(np.array(y2in))
y3i = np.float(np.array(y3in))

#Se evalua la funcion objetivo en cada vertice
fO1 = (x1i*120)+(y1i*200)
fO2 = (x2i*120)+(y2i*200)
fO3 = (x3i*120)+(y3i*200)

#coloreando la region solucion
m = [x1i, x2i, x3i]
n = [y1i, y2i, y3i]
plt.fill(m,n, color='silver')

#Calculado el mejor resultado(Minimizar)
zMin = min(fO1, fO2, fO3)

#Generando las anotaciones de la solucion optima
plt.annotate('Solucio optima: {}'.format(zMin),(x2i,y2i))


plt.show()

"""
def interseccion(x1,x2,b1,b2):
    solx = (b2 - b1)/(x1 - x2)
    soly = x1*solx+b1
    return [solx,soly]


def maxPunto(punto, x, y):
    aux = 0
    for i in punto:
        ecuacion = i[0]*x+i[0]*y
        if (ecuacion>aux):
            aux = ecuacion
    return aux

def minPunto(punto, x, y):
    aux = 0
    for i in punto:
        ecuacion = i[0]*x+i[0]*y
        if (ecuacion<aux):
            aux = ecuacion
    return aux



puntoSol.append(interseccion(2,-3,1,6))
puntoSol.append(interseccion(3,1,6,2))
puntoSol.append(interseccion(1,-6,2,3))
puntoSol.append(interseccion(6,-2,3,1))

print(maxPunto(puntoSol,1,2))
print(minPunto(puntoSol,1,2))


for i in puntoSol:
    ecuacion = i[0]*1+i[0]*2
    print(ecuacion)
    if (ecuacion>aux):
        aux = ecuacion
print(aux)
print(puntoSol)

if (ecuacion>ecuacion2):
    print("el punto maximo es: ",ecuacion)
else:
    print("el punto minimo es: ",ecuacion2)
"""
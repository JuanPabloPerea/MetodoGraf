import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

puntoSol = []

# ecuaciones e intervalos (para tabular)
# rango de la grafica .arange
x = np.arange(-10,10000,2000)
y = np.arange(-10,5000,1000)
#yMax = (-0.2*x)/0.5
y1 = (2000-0.1*x)/0.6
y2 = 6000-x
y3 = x*0
x1 = 4000+(0*y)
x2 = y*0

#Identificadores para las lineas
primerLinea = LineString(np.column_stack((x,y1)))
segundaLinea = LineString(np.column_stack((x,y2)))
tercerLinea = LineString(np.column_stack((x,y3)))
#cuartaLinea = LineString(np.column_stack((x,yMax)))
quintaLinea = LineString(np.column_stack((x1,y)))
sextaLinea = LineString(np.column_stack((x2,y)))

#Se grafican las lineas
plt.plot(x, y1, '-', color='b')
plt.plot(x, y2, '-', color='g')
plt.plot(x, y3, '-', color='y')
#plt.plot(x, yMax, '-', color='y')
plt.plot(x1, y, '-', color='k')
plt.plot(x2, y, '-', color='b')

#configuraciones adicionales del grafico
plt.grid()
plt.xlabel('Cursos de administracion')
plt.ylabel('Cursos ajenos al area de administracion')
plt.title('Metodo Grafico')

#buscando los puntos de interseccion
primerInter = tercerLinea.intersection(sextaLinea)
segundaInter = sextaLinea.intersection(primerLinea)
tercerInter = primerLinea.intersection(segundaLinea)
cuartaInter = segundaLinea.intersection(quintaLinea)
quintaInter = quintaLinea.intersection(tercerLinea)

#Graficar los vertices
plt.plot(*primerInter.xy, 'o')
plt.plot(*segundaInter.xy, 'o')
plt.plot(*tercerInter.xy, 'o')
plt.plot(*cuartaInter.xy, 'o')
plt.plot(*quintaInter.xy, 'o')

#Imprimiendo las coordenadas de los vértices en la consola
print('\n COORDENADAS DE LAS INTERSECCIONES')
print('Coordenadas de la primera intersección: {} '.format(primerInter))
print('Coordenadas de la segunda intersección: {} '.format(segundaInter))
print('Coordenadas de la tercer intersección: {} '.format(tercerInter))
print('Coordenadas de la cuarta intersección: {} '.format(cuartaInter))
print('Coordenadas de la quinta intersección: {} '.format(quintaInter))

#identificando los valores de las coordenadas x,y de cada vertice
x1in, y1in = primerInter.xy
x2in, y2in = segundaInter.xy
x3in, y3in = tercerInter.xy
x4in, y4in = cuartaInter.xy
x5in, y5in = quintaInter.xy


#Cambiar el formato de matriz a float
x1i = np.float(np.array(x1in))
x2i = np.float(np.array(x2in))
x3i = np.float(np.array(x3in))
x4i = np.float(np.array(x4in))
x5i = np.float(np.array(x5in))
y1i = np.float(np.array(y1in))
y2i = np.float(np.array(y2in))
y3i = np.float(np.array(y3in))
y4i = np.float(np.array(y4in))
y5i = np.float(np.array(y5in))

#Se evalua la funcion objetivo en cada vertice
fO1 = (x1i*0.2)+(y1i*0.5)
fO2 = (x2i*0.2)+(y2i*0.5)
fO3 = (x3i*0.2)+(y3i*0.5)
fO4 = (x4i*0.2)+(y4i*0.5)
fO5 = (x5i*0.2)+(y5i*0.5)

#coloreando la region solucion
m = [x1i, x2i, x3i, x4i, x5i]
n = [y1i, y2i, y3i, y4i, y5i]
plt.fill(m,n, color='silver')

#Calculado el mejor resultado(Minimizar)
zMax = max(fO1, fO2, fO3, fO4, fO5)

#Generando las anotaciones de la solucion optima
plt.annotate('Solucio optima: {}'.format(zMax),(x3i,y3i))


plt.show()
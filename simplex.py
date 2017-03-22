
variables = int(raw_input("Ingrese el numero de variables con las que cuenta la funcion a minimizar:"))
restricciones = int(raw_input("Ingrese el numero de restricciones con las que cuenta la funcion a minimizar:"))
A=[[0]*(variables+1) for i in range(restricciones+1)]
#A1 sera la matriz sobre la que se trabaje todo  el proceso simplex
A1=[[0]*(restricciones+1) for i in range(variables+1)]
#array_temporal=[]
#fil_pivote=[]
temporal=[]
#array_pivote=[]

print "A continuacion ingresara la funcion objetivo: "
for x in range(0,variables):
    A[restricciones][x]=float(raw_input("Ingrese el valor de X"+str(x+1)+" "))

for i in range(0,restricciones):
    if i==0:
        print "A continuacion ingresara la restriccion "+str(i+1)+": "
        for j in range(0,variables+1):
            if j==(variables):
                A[i][j]=float(raw_input("Ingrese el valor de la diferencia >=: "))
            else:
                A[i][j]=float(raw_input("Ingrese el valor de X"+str(j+1)+" "))

#transponer la lista
A1=[list(i) for i in zip(*A)]

filas=len(A1)
columnas=len(A1[0])
identidad = [[0] * (variables) for i in range(variables)]
filas1=len(identidad)
columnas1=len(identidad[1])
for i in range(0,columnas):
    for j in range(0,columnas1):
        if i==j:
            identidad[i][j]=1

matriz = [[0] * variables for i in range(1)]
identidad.append(matriz[0])

filas1=len(identidad)
columnas1=len(identidad[0])

#volver negativa la nueva funcion objetivo
for x in range(0,columnas):
    A1[filas-1][x]=-A1[filas-1][x]
#Seleccionar pivote
minimo=min(A1[filas-1])
while minimo<0:
    pos_minimo_col=A1[filas-1].index(minimo)
        for x in range(0,filas-1):
            temporal.append(A1[x][columnas-1]/A1[x][pos_minimo_col])
        minimo1=min(temporal)
        pos_minimo_fil=temporal.index(minimo1)
        val_pivote=A1[pos_minimo_fil][pos_minimo_col]
        #tenemos pocision del pivote x,y pos_minimo_fil,pos_minimo_col
        for i in range(0,columnas):
            A1[pos_minimo_fil][i]=A1[pos_minimo_fil][i]/val_pivote

        for i in range(0,columnas1):
            identidad[pos_minimo_fil][i]=identidad[pos_minimo_fil][i]/val_pivote
        for i in range(0,filas):
            cte=A1[i][pos_minimo_col]
                for j in range(0,columnas):
                    if i!=pos_minimo_fil:
                        A1[i][j]=A1[i][j]-(A1[pos_minimo_fil][j]*cte)
                for j in range(0,columnas1):
                    if i!=pos_minimo_fil:
                        identidad[i][j]=identidad[i][j]-(identidad[pos_minimo_fil][j]*cte)
        del temporal[:]
        minimo=min(A1[filas-1])
filas=len(A1)
columnas=len(A1[0])
C=A1[filas-1][columnas-1]
print "El valor de C* es: "+str(C)
tamanio1=len(identidad)
tamanio=len(identidad[tamanio1-1])
for x in range(0,tamanio):
    print "la variable X"+str(x+1)+"="+str(identidad[tamanio1-1][x])
pause = raw_input('Press ENTER to continue')

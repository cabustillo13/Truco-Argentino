import envido
import cv2

################
## cartas.txt ##
################
arreglo = list()

# Acceder a cartas.txt 
arch = open('cartas.txt', 'r')
for linea in arch:
    arreglo.append(linea)
arch.close() 

# Permite borrar \n que hay en la lista
arreglo = map(lambda s: s.strip(), arreglo) 

##########
## Main ##
##########

texto = envido.contarEnvido(arreglo[0],arreglo[1],arreglo[2])

path = "./Resultados/"
formato = ".png"

imagen = cv2.imread(path+"photo0"+formato)
fuente = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(imagen, texto, (10,365), fuente, 1, (256, 256, 256), 1)
cv2.imwrite(path+"photo1"+formato, imagen)

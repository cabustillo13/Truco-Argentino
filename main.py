import SSIM
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

#####################
## Cargar imagenes ##
#####################
# Propiedades de la imagen
path = "./Cartas/"
formato = ".png"

carta1 = cv2.imread(path+arreglo[0]+formato)
carta2 = cv2.imread(path+arreglo[1]+formato)
carta3 = cv2.imread(path+arreglo[2]+formato)

####################
## Que carta es? ##
####################
valor1 = SSIM.encontrarCarta(carta1,path,formato)
valor2 = SSIM.encontrarCarta(carta2,path,formato)
valor3 = SSIM.encontrarCarta(carta3,path,formato)

envido.contarEnvido(valor1,valor2,valor3)

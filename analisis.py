from skimage.measure import compare_ssim
import cv2

# Propiedades de la imagen
path = "./Cartas/"
formato = ".png"
nombre = "O12"

# Cargar la imagen a analizar
imagen = cv2.imread(path+nombre+formato)

# Inicializacion
score = 0                   # Score significa que no se parecen totalmente
cont = 0                    # Contador auxiliar que nos permitira determinar el numero de la imagen
palos = ["B","C","E","O"]   # B: Basto, C: Copa, E: Espada y O: Oro
i=0

while (score != 1): 

    cont = cont + 1
    
    if (cont == 8): cont= 10  # En el Truco se juega sin las cartas 8 y 9
    
    if (cont == 13):          # Las cartas de la baraja espanola llegan hasta el 12 
        cont = 1
        i=i+1
        
    palo = palos[i]
    
    nombreRef = palo+str(cont)
    # Imagen de referencia o patron a comparar
    referencia = cv2.imread(path+nombreRef+formato)

    # Convertir las imagenes a escala de grises
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    referenciaGris = cv2.cvtColor(referencia, cv2.COLOR_BGR2GRAY)

    # Calcular el indice de similitud estructural (SSIM) entre las dos imagenes
    # Devuelve la imagen con las diferencias encontradas
    (score, diff) = compare_ssim(imagenGris, referenciaGris, full=True)

# Devuelve la similitud estructural determinada
print("SSIM: {}".format(score)) 
print(nombreRef)

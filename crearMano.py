import cv2
import numpy as np

def superponerImagenes(background, overlay, x, y):

    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background 

# Crear una mano con 3 cartas distintas
path= "./Cartas/"
formato = ".png"

# Cargar imagen de fondo
fondo = cv2.imread(path+"Fondo"+formato) 

palo = ["B","C","E","O"]
numero = ["1","2","3","4","5","6","7","10","11","12"]

# Elegir aleatoriamente las 3 cartas
import random

def elegirCarta():
    return (random.choice(palo) + random.choice(numero))

nombre1 = elegirCarta()
nombre2 = elegirCarta()
nombre3 = elegirCarta()

# Corroborar que no haya cartas elegidas iguales
while (nombre1 == nombre2) or (nombre1 == nombre3) or (nombre2 == nombre3):
    if (nombre1 == nombre2): nombre1 = elegirCarta()
    if (nombre1 == nombre3): nombre1 = elegirCarta()
    if (nombre2 == nombre3): nombre2 = elegirCarta()

# Definir imagenes
img1 = cv2.imread(path+nombre1+formato)
img2 = cv2.imread(path+nombre2+formato)
img3 = cv2.imread(path+nombre3+formato)

aux = superponerImagenes(fondo,img1,7,15)
aux = superponerImagenes(aux, img2, 217,15)
aux = superponerImagenes(aux, img3, 427,15)

cv2.imwrite("./Resultados/photo0.png", aux)

# Bibliografia: https://www.it-swarm.dev/es/python/usando-opencv-para-superponer-una-imagen-transparente-en-otra-imagen/829146437/

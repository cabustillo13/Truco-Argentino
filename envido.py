def extraerDatos(dato):
    
    palo = dato[0:1]        # Se extrae el primer caracter correspondiente a un palo
    aux = dato.split(palo)
    valor = int(aux[1])     # Se extra el valor del caracter

    if (valor >= 10):       # En el envido las cartas de 10 para arriba suman cero      
        valor = 0
    
    return palo, valor

def contarEnvido(carta1,carta2,carta3):
    
    palo1, aux1 = extraerDatos(carta1)
    palo2, aux2 = extraerDatos(carta2)
    palo3, aux3 = extraerDatos(carta3)

    if ((palo1 == palo2) and (palo2 == palo3)):
        #print("Flor")       # Flor significa que las 3 cartas son del mismo palo
        
        suma = 20 + aux1+aux2+aux3
        
        if suma > 33:       # La maxima suma que se puede realizar con la flor es 33
            auxMax = max([aux1,aux2,aux3])
            auxMin = min([aux1,aux2,aux3])
            
            if ((aux1 > auxMin) and (aux1 < auxMax)): suma = 20 + aux1 + auxMax
            if ((aux2 > auxMin) and (aux2 < auxMax)): suma = 20 + aux2 + auxMax
            if ((aux3 > auxMin) and (aux3 < auxMax)): suma = 20 + aux3 + auxMax
        
        texto = "FLOR. La suma de la flor es: " + str(suma)
        #print("La suma de la flor es: {}".format(suma))
        
    elif ((palo1 == palo2) and (palo2 != palo3)):
        suma = 20 + aux1 + aux2
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))

    elif ((palo1 == palo3) and (palo1 != palo2)):
        suma = 20 + aux1 + aux3
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
        
    elif ((palo2 == palo3) and (palo1 != palo2)):
        suma = 20 + aux2 + aux3
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
        
    else:
        #print("Mentiste. No tenias nada para el envido")
        suma = max([aux1,aux2,aux3])
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
    
    
    return texto
        

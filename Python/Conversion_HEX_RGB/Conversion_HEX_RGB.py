conversion = lambda numero_hex: int(numero_hex, 16)

def hex_string_to_RGB(hex_string : str) -> dict:
    
    # divido por trozos 
    rojo, verde, azul= [hex_string[1:3], hex_string[3:5], hex_string[5:]] # en el ultimo es 5: porque  es desde la pos 5 hasta el final
        
    return {
        "r" : conversion(rojo), # int(valor,base a convertir)
        "g" : conversion(verde), 
        "b" : conversion(azul)
    }
def somar(a,b):
    calculo = a+b
    return calculo

def sub(a,b):
    calculo = a-b
    return calculo

def mult(a,b):
    calculo = a*b
    return calculo

def div(a,b):
    calculo = a/b
    return calculo

def pares(a,b):
    if (a < b):
        inicio = a
        fim = b
    else:
        inicio = b
        fim = a
    contador = inicio
    lista_pares = []
   
    while contador<= fim:
        if contador % 2 == 0:
            lista_pares.append(contador)
        contador += 1
    return lista_pares
             
        

def impar(a,b):
    if (a < b):
        inicio = a
        fim = b
    else:
        inicio = b
        fim = a
    
    contador = inicio
    lista_impar =[]
    
    while contador<= fim:
        if contador % 2 == 1:
            lista_impar.append(contador)        
        contador += 1
        
        
        
    return lista_impar
# Cristhian Erick De La Rosa Muñoz  Folio:1064XR06


print("\tImprime una cuenta de numeros primos\n\n")
limite=int(input("Indica el limite de la cuenta: "))
print("\n")
primos=[]
conteo=1

while len(primos)<limite+1:  # Se repite hasta que la lista primos este completa
    
    if conteo<4:           #Agrega de forma inmediata 1,2,3
        primos.append(conteo)
    elif conteo>3:
        pase=True
        rep=True
        n=1
        b=len(primos)
        while rep:
            a=conteo%primos[n]
            if a==0:
                pase=False
            n+=1
            if pase!=rep or n==b:
                rep=False
        if pase:
            primos.append(conteo)
    conteo+=1
print("Lista de numeros los primeros ",limite," numeros primos:\n")
print(primos[1:])

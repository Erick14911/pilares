#Imprime un triangulo de caracteres
#Usando una funcion

import sys
def triangulo(h,c):
    r=1
    for i in range(0,h):
        print("")
        if r<=h:
            for j in range(0,r):
                print(c,end=" ")
            r+=1
    

print("Formaremos un triangulo rectangulo")
#h=int(input("Ingresa la longitud de sus catetos: "))
#c=input("ingresa el caracter: ")
h=int(sys.argv[1])
c=sys.argv[2]
triangulo(h,c)

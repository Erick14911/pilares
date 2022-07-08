# Programa
####
########
############

l=int(input("Ingresa la longitud de los lados del cuadrado: "))

for n in range(0,l):
####
    print("")
    for m in range(0,l):
########
        print("*",end=" ")
print("\n\n")
print("Formaremos un triangulo rectangulo")
h=int(input("Ingresa la longitud de sus catetos: "))

r=1
for i in range(0,h):
####
    print("")
    if r<=h:
########
        for j in range(0,r):
############
            print("*",end=" ")
        r+=1
print("\n\n")
print("Formaremos un triangulo rectangulo")
b=int(input("Ingresa la longitud de sus catetos: "))
q=0
z=b
for k in range(0,b):
    print("")
    for x in range(0,q):
        print(" ",end=" ")
    for y in range(0,z):
        print("*",end=" ")
    q+=1
    z-=1

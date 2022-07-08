import sys
def suma(a,b):
    c=a+b
    return c
def resta():
    

print("Suma los numeros")
#num1=float(input("Ingrasa A: "))
#num2=float(input("Ingresa B: "))
num1=int(sys.argv[1])
num2=int(sys.argv[2])

    
resultado=suma(num1,num2)    
print("El resultado es: ",resultado)


def dic():
    registro={}

    nombre=input("Nombre: ")
    age=float(input("\nIngresa su edad: "))
    while age<=0:
        age=float(input("\nIngresa su edad: "))
    registro[nombre]=age
    return regisro

registro={}    
n=int(input("\n¿Cuantos alumnos registraras?"))
for i in range(0,n):
    dic()
    registro=dic()
    
for k in range(0,len(registro)):
     lista[0:len(registro[claves[k]])]=registro[claves[k]]
     promedio=sum(lista)/len(lista)                                           
     print(claves[k]," calificacion promedio ",promedio)

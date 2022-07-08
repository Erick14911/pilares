# CristhianErick De La Rosa Muñoz Folio: 1064XR06

#**5.- Codifica un programa en python que nos permita guardar los nombres de
#los alumnos de una clase y las notas que han obtenido. Cada alumno puede
#tener distinta cantidad de notas. Guarda la información en un diccionario cuya
#claves serán los nombres de los alumnos y los valores serán listados con las
#notas de cada alumno.

#El programa pedirá el número de alumnos que vamos a introducir,
#pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un
#número negativo. Al final el programa nos mostrará la lista de alumnos y la nota
#media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno
#que ya existe el programa nos dará un error.**

registro={}
notas=[]
alumnos=[]
claves=[]
lista=[]

n=int(input("\n¿Cuantos alumnos ingresaras? "))

for i in range(0,n):
    pase=True

    alumno=input("\nIngresa un nombre: ")   
    alumnos.append(alumno)
    if alumnos.count(alumno)>1:
        print("Error: Este nombre se repite")
    else:
        while pase==True:
            nota=float(input("\nIngresa su nota: "))
            if nota<0:
                pase=False
            else:
                notas.append(nota)           

    registro[alumnos[i]]=notas[:]
    del notas[:]
        
print("\n")
claves[0:len(registro)]=registro

for k in range(0,len(registro)):
     lista[0:len(registro[claves[k]])]=registro[claves[k]]
     promedio=sum(lista)/len(lista)                                           
     print(claves[k]," calificacion promedio ",promedio)

#Cristhian Erick De La Rosa Muñoz Folio:1064XR06
#
# 3.- Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
# (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
# la nota más alta que ha sacado y la menor.

lista3=[]
for k in range(0,5):
    nota=int(input("Ingresa la nota del alumno: "))
    if (nota>=0 or nota<=10):
        lista3.append(nota)


suma=0
for nota in  range(0,5):
    suma+=int(lista3[nota])

media=suma/5
print("Sus notas fueron: ",lista3[:])
print("La suma total de sus notas es: ",suma)
print("La media de sus notas es: ",media)
mayor=sorted(lista3,reverse=True)
print("La mayor calificacion fue: ",mayor[0])
menor=sorted(lista3)
print("La menor calificacion fue: ",menor[0])

     
#print("Su mayor nota es: ",mayor[0]," y la menor es: ",menor[0])




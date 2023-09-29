from io import open

def agregar_tarea(*tareas):
    fichero = open ('tareas.txt','a') #
    for i in tareas: 
        fichero.write(i + '\n') #Escribir texto


def listar_tareas():
    indice=1
    with open('tareas.txt', 'r') as fichero:
        print("----------TAREAS LISTADAS----------")
        for i in fichero:
            print(f"{indice} . {i.strip()}")
            indice+=1

    indice=0
    with open("tareas_completadas.txt","r") as fichero2:
        print("----------TAREAS TERMINADAS----------")
        for e in fichero2:
            print(f"{indice} . {e.strip()}")
            indice+=1

def marcar_complete():
    fichero=open('tareas.txt','r+')
    lineas=fichero.readlines()
    tarea= int(input("Ingrese el numero de la tarea que desea borrar: "))
    fichero2=open("tareas_completadas.txt","a")
    fichero2.write(lineas[tarea-1])
    del(lineas[tarea-1])
    fichero.seek(0)
    fichero.writelines(lineas)
 
numero_tareas=int(input("Ingrese el numero de tarea que agregaras: "))   
for i in range (numero_tareas):
    agregar_tarea(input("Escribe una tarea: "))
   
agregar_tarea()
listar_tareas()
marcar_complete()
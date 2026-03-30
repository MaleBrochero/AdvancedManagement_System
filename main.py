
import servicios 


#### Sistema para gestionar la informacion basica de los estudiante.

bienvenido = (f"""Bienvenido al sistema de gestion estudiantil:
                   Marque una opcion:
                    1.Continuar 
                    2.Salir  """) 

while bienvenido == "1":
    
    menu = input(f"""Elija una de las siguientes opciones :
                 1. Registar
                 2. Consultar
                 3. Atualizar
                 4.Eliminar estudiante\n""")
    
    if menu == "1" :
        id_estudiante = input("Por favor agregue ID del estudiante")
        nombre = input("Por favor agregue el nombre del estudiante")
        edad = input ("Por favor agregue la edad del estudiante")
        programa = input("Por favor agregue el nombre del programa al que pertenezc el estudiante")
        estado = input("Por favor escriba el estado del estudiante activo o inactivo")
        
        servicios.agregar_estudiante(id_estudiante, nombre, edad, programa,estado)


    elif menu == "2" :
         
         servicios.mostar_estudiante()

    elif menu == "3" :

        servicios.actualizar_estudiante ()
        
    elif menu == "4" :
        servicios.eliminar_estudiante ()

    else :
        print(" Opcion invalida vuelva a intentar ")
print(" Ha salido correctamente del programa ")
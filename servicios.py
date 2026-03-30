lista_estudiante = []

def agregar_estudiante ( a, b,c,d,e) :
        
        estudiante = {
         "ID"   :  a,
        "Nombre": b,
        "Edad": c,
        "Programa": d,
        "Estado" : e
    }
        
        lista_estudiante.append(estudiante)

        print("ID " + a + " agregado correctamente.")


def mostar_estudiante():
        
        if len(lista_estudiante) == 0:
            print("El inventario esta vacio.")
        

        else:
            print ( lista_estudiante)
        return


def actualizar_estudiante ():
        
            
        actualizar = input(f"""Marque la opcion que dedecia actualizar
                            1. ID    
                            2. Nombre
                            3. Edad
                            4. Programa
                            5. Estado \n""")
        
        

        if actualizar == "1"  :

            validacion_ID = input(" Por favor ingrese la ID antigua del estudiante al que desea actualizar")
            actualizado_ID = input(" Por favor ingrese el nuevo ID ")
            
            for estudiante in lista_estudiante:

                if len(lista_estudiante) == 0:
                    print("Estudiante con ID" + validacion_ID + " no encontrado. Lista Vacia .")
                    return

                if estudiante ["ID"] == validacion_ID:

                    estudiante["ID"] = actualizado_ID
                    print("Estudiante con ID " + actualizado_ID  + " fue actualizado.")
                    return 

            

        elif actualizar == "2" :

            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar")
            actualizado_nombre = input(" Por favor ingrese el nuevo Nombre ")
            for estudiante in lista_estudiante:

                if len(lista_estudiante) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if estudiante ["ID"] == validacion_ID:

                    estudiante["Nombre"] = actualizado_nombre
                    print("Estudiante con ID " + actualizado_nombre  + " fue actualizado.")
                    return 
                


        
        elif actualizar == "3" :
            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar")
            actualizado_edad = input(" Por favor ingrese la nueva Edad ")
            
            for estudiante in lista_estudiante:

                if len(lista_estudiante) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if estudiante ["ID"] == validacion_ID:

                    estudiante["Edad"] = actualizado_edad
                    print("Estudiante con nombre " + actualizado_edad + " fue actualizado.")
                    return 
                

        
        elif actualizar == "4" :

            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar")
            actualizado_programa = input(" Por favor ingrese el nuevo Programa")

            for estudiante in lista_estudiante:

                if len(lista_estudiante) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if estudiante ["ID"] == validacion_ID:

                    estudiante["Programa"] = actualizado_programa
                    print("Estudiante con ID " + validacion_ID  + " fue actualizado.")
                    return 
                

        
        
        elif actualizar == "5" :
            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar")
            actualizado_estado = input(" Por favor ingrese el nuevo Estado ")

            for estudiante in lista_estudiante:

                if len(lista_estudiante) == 0:
                    print("Estudiante con nombre " + validacion_ID + " no encontrado. Lista Vacia.")
                    return
            
                if estudiante ["ID"] == validacion_ID:

                    estudiante["Estado"] = actualizado_estado
                    print("Estudiante con ID " + validacion_ID  + " fue actualizado.")
                    return 
                

            
        
        else :
            print(" Opcion invalida vuelva a intentar ")
            return


def eliminar_estudiante ():
      
    estudiante_eliminar = input("Por favor la ID del estudiante a eliminar ")

    for estudiante in lista_estudiante:

        if len(lista_estudiante) == 0:
            print("Estudiante con ID" + estudiante_eliminar + " no encontrado. Nada que eliminar.")
            return

        if estudiante ["ID"] == estudiante_eliminar: 
        
            lista_estudiante.remove(estudiante_eliminar )
            print("Estudiante con ID " + estudiante_eliminar  + " eliminado del inventario.")
            return
        






              
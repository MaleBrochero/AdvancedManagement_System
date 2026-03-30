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
        
        if actualizar == "1" :
              actualizado_ID = input(" Por favor ingrese el nuevo ID ")
              
        elif actualizar == "2" :
              actualizado_nombre = input(" Por favor ingrese el nuevo Nombre ")
        
        elif actualizar == "3" :
              actualizado_edad = input(" Por favor ingrese la nueva Edad ")
        
        elif actualizar == "4" :
              actualizado_programa = input(" Por favor ingrese el nuevo Programa")
        
        
        elif actualizar == "5" :
              actualizado_estado = input(" Por favor ingrese el nuevo Estado ")
        
        else :
            print(" Opcion invalida vuelva a intentar ")
        return

def eliminar_estudiante ():
      
      estudiante_eliminar = input("Por favor la ID del estudiante a eliminar ")
              
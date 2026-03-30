student_list = []

def  add_student ( a, b,c,d,e) :
        
        student = {
         "ID"   :  a,
        "Name": b,
        "Age": c,
        "Program": d,
        "Status" : e
    }
        
        student_list.append(student)

        print("ID " + a + " added successfully .")


def show_student(): 
        
        if len(student_list) == 0:
            print(" Empty student list. ")
        

        else:
            print (student_list)


def  update_student():
        
            
        update = input(f"""Select the option that says "update"

                                1. ID

                                2. Name

                                3. Age

                                4. Program

                                5. Status\n""")
        
        

        if update == "1"  :

            ID_validation = input(" Por favor ingrese la ID antigua del estudiante al que desea actualizar ")
            ID_updated = input(" Por favor ingrese el nuevo ID ")
            
            for student in student_list:

                if len( student_list) == 0:
                    print("Estudiante con ID" +  + " no encontrado. Lista Vacia .")
                    return

                if student ["ID"] == ID_validation:

                    student["ID"] = ID_updated
                    print("Student ID " + ID_validation  + " updated.")
                    return 

            

        elif update == "2" :

            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar ")
            actualizado_nombre = input(" Por favor ingrese el nuevo Nombre ")
            for student in student_list :

                if len(student_list) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if student["ID"] == validacion_ID:

                    student["Name"] = actualizado_nombre
                    print("Estudiante con ID " + actualizado_nombre  + " fue actualizado.")
                    return 
                


        
        elif update == "3" :
            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar ")
            actualizado_edad = input(" Por favor ingrese la nueva Edad, solo numeros ejem : 12, 14, 22 ....")
            
            for student in student_list:

                if len(student_list) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if student ["ID"] == validacion_ID:

                    student["Age"] = actualizado_edad
                    print("Estudiante con nombre " + actualizado_edad + " fue actualizado.")
                    return 
                

        
        elif update == "4" :

            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar ")
            actualizado_programa = input(" Por favor ingrese el nuevo Programa")

            for student in student_list:

                if len(student_list) == 0:
                    print("Estudiante con ID " + validacion_ID + " no encontrado. Lista Vacia.")
                    return

                if student["ID"] == validacion_ID:

                    student["Program"] = actualizado_programa
                    print("Estudiante con ID " + validacion_ID  + " fue actualizado.")
                    return 
                

        
        
        elif update == "5" :
            validacion_ID = input(" Por favor ingrese la ID del estudiante al que desea actualizar ")
            actualizado_estado = input(" Por favor ingrese el nuevo Estado ")

            for student in student_list:

                if len(student_list) == 0:
                    print("Estudiante con nombre " + validacion_ID + " no encontrado. Lista Vacia.")
                    return
            
                if student ["ID"] == validacion_ID:

                    student["Status"] = actualizado_estado
                    print("Estudiante con ID " + validacion_ID  + " fue actualizado.")
                    return 
                

            
        
        else :
            print(" Opcion invalida vuelva a intentar ")
            return


def eliminar_estudiante ():
      
    estudiante_eliminar = input("Por favor la ID del estudiante a eliminar ")

    if len(student_list) == 0:
        print("Estudiante con ID" + estudiante_eliminar + " no encontrado. Nada que eliminar.")
        return

    for student in student_list:

    
        if student["ID"] == estudiante_eliminar: 
        
            student_list.remove(student)
            print("Estudiante con ID " + estudiante_eliminar  + " eliminado del inventario.")
            return
        






              
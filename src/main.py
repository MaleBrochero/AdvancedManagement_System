
import servicios 


#### Sistema para gestionar la informacion basica de los estudiante.

welcome = input(f"""Welcome to the student management system:
                    1.Continue 
                    1=!.Exit\n  """) 

while welcome == "1":
    
    menu = input(f"""Choose one of the following options:

                        1. Register

                        2. View

                        3. Update

                        4. Delete student\n""")
    
    if menu == "1" :
        student_id = input(" Please add student ID ")
        name = input("Please add the student's name ")
        age = input ("Please add the student's age ")
        program = input("Please add the name of the program the student belongs to ")
        status = input(" Please write the student's status: active or inactive ")
        
        servicios.agregar_estudiante(student_id, name, age, program, status)


    elif menu == "2" :
         
         servicios.mostar_estudiante()

    elif menu == "3" :

        servicios.actualizar_estudiante ()
        
    elif menu == "4" :
        servicios.eliminar_estudiante ()

    else :
        print(" Invalid option, please try again  ")

print("It has successfully exited the program ")

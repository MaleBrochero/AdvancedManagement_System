# AdvancedManagement_System
This system allows you to identify a student's status.

## *Use of the program*  
_This program allows you to manage basic student information.
The system allows you to register, view, update, and delete students, as well as store the information in a structured way for later use.._

*The program operates through an interactive menu with the following options:

* Add Student: Registers a new student with their ID, name, age, program, and status.

* Show Student: Displays all registered students, showing their ID, name, age, program, and status.

* Update: Allows you to modify ID, name, age, program, and status.

* Delete: Permanently deletes a student and all their data from the registry.

* Exit: Securely closes the program.

# Requisitos
_Python 3.14 installed on your system_


# How do I run the program?

Windows
_py src\app.py_

# Project Structure
_The code is modularized to maintain good development practices:

src/app.py: Main file that starts the program, contains the infinite loop, and manages the interactive menu with input validations (try/except).

src/servicios.py: Logic module that contains all inventory operations (CRUD, console printing, and statistics calculation)_
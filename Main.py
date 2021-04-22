from ClaseAlumno import Alumno

def Opcion0():
    print(Alumno.maxInasistencias)
    contTotal = 0
    cont = 0
    print("Ingrese año y divison:")
    year = int(input("año: "))
    division = str(input("division: "))

    for indice, alumno in enumerate(ListaAlumnos):
        contTotal += 1
        if alumno.get_year() == year and alumno.get_division() == division:
            if alumno.get_inasistencias() > Alumno.maxInasistencias:
                cont += 1
                print(alumno.get_nombre())
    total = (cont * 100) / contTotal
    print(f"El porcentaje de alumnos que superan el maximo de inasistencias es de {total} %")

def Opcion1():
    print("Ingrese nuevo maximo de inasistencias permitidas")
    inasistancias = int(input("nuevo valor: "))
    Alumno.maxInasistencias = inasistancias
    print(Alumno.maxInasistencias)

switcher = {
    0: Opcion0,
    1: Opcion1
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__=='__main__':
    ListaAlumnos = []
    MAlumno = Alumno(0, 0, 0, 0)
    ListaAlumnos = MAlumno.Carga()

    bandera = False
    while not bandera:
        print("MENU DE OPCIONES")
        print("0: Ingrese año y division para indicar nombre de alumno y porcentaje de alumnos que superan el maximo de inasistencias")
        print("1: Modificar el maximo de inasistencias")
        print("3: Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 3:
            bandera = True
        else:
            switch(opcion)
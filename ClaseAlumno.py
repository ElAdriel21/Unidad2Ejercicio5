import csv

class Alumno:
    __nomb = ""
    __year = ""
    __division = ""
    __inasistencias = 0
    maxInasistencias = 15
    clases = 5

    def __init__(self, v1, v2, v3, v4):
        self.__nomb = v1
        self.__year = v2
        self.__division = v3
        self.__inasistencias = v4

    def Carga(self):
        MAlumnos = []
        archivo1 = open("archivo.csv")
        reader = csv.reader(archivo1, delimiter=",")
        for fila in reader:
            d0 = str(fila[0])  # Nomb
            d1 = int(fila[1])  # year
            d2 = str(fila[2])  # Division
            d3 = int(fila[3])  # Inasistencias
            if type(d0) == str and type(d1) == int and type(d2) == str and type(d3) == int:
                v1 = Alumno(d0, d1, d2, d3)
                MAlumnos.append(v1)
                print(f"{v1} |  cargado")
        archivo1.close()
        return (MAlumnos)

    def get_year(self):
        return self.__year

    def get_division(self):
        return self.__division

    def get_inasistencias(self):
        return self.__inasistencias

    def get_nombre(self):
        return self.__nomb

    def __str__(self):
        return (f"{self.__nomb:20} | {self.__year:1} | {self.__division:1} | {self.__inasistencias:3}")
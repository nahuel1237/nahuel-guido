from PySide2.QtWidgets import QTableWidgetItem


class Alumno:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.grupo = None


    def convertir_a_qt(self):
        return[
            (0, QTableWidgetItem(str(self.nombre))),
            (1, QTableWidgetItem(str(self.apellido))),
            (2, QTableWidgetItem(str(self.dni))),
            (3, QTableWidgetItem(repr(self.grupo))),
        ]

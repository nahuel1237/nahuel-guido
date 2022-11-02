from PySide2.QtWidgets import QMainWindow

from ui_windows.general import Ui_MainWindow

from py_windows.window_alumno import AlumnoWindow
from py_windows.grupo import GrupoWindow
from py_windows.tabla import TablaWindow


class GeneralWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.lista_alumnos = []

        self.alumno_window = AlumnoWindow(self.lista_alumnos)
        self.tabla_window = TablaWindow(self.lista_alumnos)
        self.grupo_window = GrupoWindow()

    def ing_alum(self):
        self.alumno_window.show()

    def crea_grup(self):
        self.grupo_window.show()

    def lista_alum(self):
        self.tabla_window.show()
        print(self.lista_alumnos)
    def salir(self):
        exit()



from PySide2.QtWidgets import QMainWindow

from utils.alumno import Alumno
from ui_windows.ingresar_alumno import Ui_MainWindow


class AlumnoWindow(QMainWindow):
    def __init__(self, ref_lista_alumnos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ref_lista_alumnos = ref_lista_alumnos

    def limpiar_alum(self):
        self.ui.le_nombre1.setText('')
        self.ui.le_apellido1.setText('')
        self.ui.le_DNI_1.setText('')

    def enviar_alum(self):
        nombre = self.ui.le_nombre1.text()
        apellido = self.ui.le_apellido1.text()
        dni = self.ui.le_DNI_1.text()
        alumno = Alumno(nombre, apellido, dni)
        self.ref_lista_alumnos.append(alumno)
        self.limpiar_alum()

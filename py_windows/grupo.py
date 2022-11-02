from PySide2.QtWidgets import QMainWindow
from utils.grupos import Grupo
from ui_windows.grupo import Ui_MainWindow


class GrupoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def limpiar_grup(self):
        self.ui.le_nombre_2.setText('')
        self.ui.le_descrip_2.setText('')
    def enviar_grup(self):
        nombre= self.ui.le_nombre_2.text()
        descripcion=self.ui.le_descrip_2.text()
        self.grupos.append(Grupo(nombre,descripcion))
        print(self.grupos)
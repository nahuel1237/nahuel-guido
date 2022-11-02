from PySide2.QtWidgets import QMainWindow

from ui_windows.tabla import Ui_MainWindow


class TablaWindow(QMainWindow):
    def __init__(self, ref_list_alumnos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ref_list_alumnos=ref_list_alumnos
    def showEvent(self, event):
        super().showEvent(event)
        print(self.ref_list_alumnos)

    def buscar_tab(self):
        pass

    def borrar_tab(self):
        pass

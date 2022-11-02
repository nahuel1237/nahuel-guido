class Grupo:
    def __int__(self, nombre, descripcion):
        self.nombre = nombre.capitalize()
        self.descripcion= descripcion.capitalize()

    def __str__(self):
        return f'{self.nombre}: {self.descripcion}'

    def __repr__(self):
        return str(self.nombre)
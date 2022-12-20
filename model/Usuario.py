class Usuario:
    def __init__(self, id, nombre, fecha_inicio, salario):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.salario = salario

    def __str__(self):
        str_usuario=f"Id:{self.id}"
        str_usuario+="\n"
        str_usuario+=f"Nombre:{self.nombre}"
        str_usuario+="\n"
        str_usuario+=f"Fecha:{self.fecha_inicio.day}/{self.fecha_inicio.month}/{self.fecha_inicio.year}"
        str_usuario+="\n"
        str_usuario+=f"Salario:{self.salario}"
        return str_usuario
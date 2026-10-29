class Usuario:
    def __init__(self, nombre, edad, correo, contrasena):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.contrasena = contrasena

    def datos_completos(self):
        if self.nombre != "" or self.edad != "" or self.correo != "" or self.contrasena != "":
            return True
        else:
            return False
        
    def correo_valido(self):
        if self.correo[len(self.correo) - 13 : len(self.correo)] == "@pioix.edu.ar":
            return True
        else:
            return False
        
    def nombre_valido(self):
        if self.nombre.isalpha():
            return True
        else:
            return False
        
    def contrasena_correcta(self, contrasena):
        if contrasena == self.contrasena:
            return True
        else:   
            return False

       
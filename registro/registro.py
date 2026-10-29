import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from clases.usuario import Usuario  
# Carga el archivo registro.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "registro.kv"))


# El nombre de esta clase (RegistroScreen) es el mismo que aparece entre < > en registro.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class RegistroScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"
    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def registrar(self):
        # Por ahora no se guarda nada: cualquier dato entra.
        # En la clase 3 acá se va a guardar el usuario nuevo.
        app = MDApp.get_running_app()
        nombre = self.ids.nombre.text
        edad = self.ids.edad.text
        correo = self.ids.correo.text
        contrasena = self.ids.contrasena.text
        nuevo = Usuario(nombre, edad, correo, contrasena)
        if not nuevo.datos_completos():
            print("Registro inválido: hay campos sin completar")
            return
        if not nuevo.correo_valido():
            print("Registro inválido: el correo debe terminar en @pioix.edu.ar")
            return
        if not nuevo.nombre_valido():
            print("Registro inválido: el nombre debe contener solamente letras")
            return  
        for usuario in app.usuarios:
            if usuario.correo == correo:
                print("Registro inválido: el correo ya está registrado")
                return
        app.usuarios.append(nuevo)
        print("Registro válido")
        self.manager.current = "login"      
    
        


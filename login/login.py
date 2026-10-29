import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

# Carga el archivo login.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))


# El nombre de esta clase (LoginScreen) es el mismo que aparece entre < > en login.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class LoginScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"


    # Se ejecuta cuando en el .kv se escribe root.iniciar_sesion()
    def iniciar_sesion(self):
        app = MDApp.get_running_app()
        correo = self.ids.correo.text.strip()
        contrasena = self.ids.contrasena.text
        if not correo or not contrasena:
            print("Inicio de sesión inválido: faltan datos")
            return
        for usuario in app.usuarios:
            if usuario.correo == correo:
                if usuario.contrasena_correcta(contrasena):
                    app.usuario_actual = usuario
                    print("Inicio de sesión válido")
                    self.manager.current = "home"
                    return
                print("Inicio de sesión inválido: contraseña incorrecta")
                return
        print("Inicio de sesión inválido: el correo no está registrado")
        # Por ahora no se guarda nada: cualquier dato entra.
        # En la clase 3 acá se va a guardar el usuario nuevo.

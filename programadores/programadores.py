import os

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen

# Carga el archivo programadores.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "programadores.kv"))

# Carpeta con las imágenes del proyecto (está al lado de esta carpeta)
CARPETA_IMAGENES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")

# Integrantes del grupo. Cambien los datos por los de ustedes.
# "foto" es el nombre del archivo de la foto, que tiene que estar en la carpeta images.
INTEGRANTES = [
    {"nombre": "Nicolás Nahuel Degdeg", "curso": "4ºB INFO", "foto": "nico.jpg"},
    {"nombre": "Manuel Benicio Di Oduardo Laredo", "curso": "4ºB INFO", "foto": "manu.jpg"},
    {"nombre": "Manuel Pérez Fernández", "curso": "4ºB INFO", "foto": "perez.jpg"},
    {"nombre": "Matías Nahuel Schendel", "curso": "4ºB INFO", "foto": "mati.jpg"},
]


class TarjetaIntegrante(MDCard):
    # Datos que muestra cada tarjeta (se usan en programadores.kv)
    nombre = StringProperty()
    curso = StringProperty()
    foto = StringProperty()


class ProgramadoresScreen(MDScreen):
    def on_kv_post(self, base_widget):
        # Se ejecuta una vez, cuando la pantalla ya está armada:
        # crea una tarjeta por cada integrante de la lista.
        for integrante in INTEGRANTES:
            tarjeta = TarjetaIntegrante(
                nombre=integrante["nombre"],
                curso=integrante["curso"],
                foto=os.path.join(CARPETA_IMAGENES, integrante["foto"]),
            )
            self.ids.lista.add_widget(tarjeta)

    def volver(self):
        self.manager.current = "inicio"

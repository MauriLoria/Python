import tkinter as tk
import customtkinter as ctk
import os
from PIL import ImageTk, Image

# Carpetas
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
# C:\MegaMauri\Aceros Felo
# Mode de color y tema
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class Login:
    def __init__(self):
        # Ventana principal
        self.root = ctk.CTk()        
        self.root.title("Aceros Felo")
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "FELO.PNG"))
        self.root.geometry("400x500")
        self.root.resizable(False, False) # Bloqueo las dimensiones de la ventana

        # Ventana principal
        logo = ctk.CTkImage(
            light_image = Image.open((os.path.join(carpeta_imagenes, "FELO.PNG"))), # Imagen modo claro
            dark_image = Image.open((os.path.join(carpeta_imagenes, "FELO.PNG"))),  # Imagen modo oscuro
            size = (200, 200))

        etiqueta = ctk.CTkLabel(master = self.root, 
                        image=logo,
                        text="")
        etiqueta.pack(pady = 15)

        # campos de texto (usuario)
        ctk.CTkLabel(self.root, text="Usuario").pack()
        self.usuario = ctk.CTkEntry(self.root)
        self.usuario.insert(0, "")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, 'end'))
        self.usuario.pack()

        # contraseña
        ctk.CTkLabel(self.root, text="Contraseña").pack()
        self.contraseña = ctk.CTkEntry(self.root)
        self.contraseña.insert(0, "*******")
        self.contraseña.bind("<Button-1>", lambda e: self.contraseña.delete(0, 'end'))
        self.contraseña.pack()

        # Botón de envío
        ctk.CTkButton(self.root, text="Entrar", command=self.validar).pack(pady = 20)

        self.root.mainloop()

    # Función para validar el login
    def validar(self):
        obtener_usuario = self.usuario.get()
        obtener_contrasena = self.contraseña.get()
        if obtener_usuario != "MauriLoria" or obtener_contrasena != "171274":
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            self.info_login.pack()
        else:
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self.info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
            self.info_login.pack()

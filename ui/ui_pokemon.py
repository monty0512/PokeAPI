import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import requests
from requests.exceptions import ConnectionError

try:
    r = requests.get("http://127.0.0.1:8000/", timeout=3)
except ConnectionError:
    # muestra mensaje: "Inicia la API primero"
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error de conexión", "Inicia la API primero")
    exit(1)

# URL base del backend FastAPI
API_BASE = "http://127.0.0.1:8000"

# Clase principal de la aplicación Tkinter
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Pokemon UI")
        self.geometry("420x520")

        # Variable para mantener la referencia de la imagen
        self.photo = None

        # Variable para almacenar el ID ingresado
        self.id_var = tk.StringVar(value="25")

        # Frame superior con el formulario
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        # Etiqueta, campo de texto y botón
        ttk.Label(top, text="Pokemon ID:").pack(side="left")
        ttk.Entry(top, textvariable=self.id_var, width=10).pack(side="left", padx=8)
        ttk.Button(top, text="Buscar", command=self.load_pokemon).pack(side="left")

        # Etiqueta para mostrar la información del Pokémon
        self.info = ttk.Label(self, text="", padding=10, justify="center")
        self.info.pack(fill="x")

        # Etiqueta donde se mostrará la imagen
        self.img_label = ttk.Label(self)
        self.img_label.pack(pady=10)

    # Función para cargar la información del Pokémon
    def load_pokemon(self):
        pid = self.id_var.get().strip()

        # Validar que el ID sea numérico
        if not pid.isdigit():
            messagebox.showerror("Error", "El ID debe ser un número.")
            return

        try:
            # Solicitar información al backend
            r = requests.get(f"{API_BASE}/pokemon/{pid}", timeout=10)
            r.raise_for_status()
            data = r.json()

            # Mostrar información del Pokémon
            self.info.config(
                text=f"#{data['id']}  {data['name'].title()}\n"
                     f"Height: {data['height']}  Weight: {data['weight']}"
            )

            # Descargar la imagen del Pokémon
            ir = requests.get(data["image_url"], timeout=10)
            ir.raise_for_status()

            # Procesar la imagen para mostrarla en Tkinter
            img = Image.open(BytesIO(ir.content)).convert("RGBA")
            img = img.resize((280, 280))

            self.photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=self.photo)

        except Exception as e:
            # Mostrar cualquier error ocurrido
            messagebox.showerror("Error", str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    App().mainloop()

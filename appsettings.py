import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Settings:
    # URL base de la API externa
    API_URL: str = os.getenv("API_URL")
    
    # URL base para las imágenes de los Pokémon
    IMG_URL: str = os.getenv("IMG_URL")

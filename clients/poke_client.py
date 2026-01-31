import httpx
from appsettings import Settings

# Cliente encargado de comunicarse con la API externa
class PokeClient:
    def __init__(self):
        # Cargar las configuraciones desde las variables de entorno
        self.settings = Settings()

    # Obtener la información del Pokémon por su ID
    async def get_pokemon_id(self, pokemon_id: int) -> httpx.Response:
        # Construir la URL de la API usando el ID
        url = self.settings.API_URL.format(id=pokemon_id)

        # Realizar la petición HTTP a la API externa
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response
    
    # Obtener la imagen del Pokémon por su ID
    async def get_pokemon_image(self, pokemon_id: int) -> httpx.Response:
        # Construir la URL de la imagen usando el ID
        url = self.settings.IMG_URL.format(id=pokemon_id)

        # Realizar la petición HTTP para descargar la imagen
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response

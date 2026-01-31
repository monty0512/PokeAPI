import httpx
from fastapi import HTTPException
from clients.poke_client import PokeClient
from DTOs.poke_dto import PokemonResponseDTO   
from appsettings import Settings

# Clase que contiene la lógica de negocio de Pokémon
class PokeServices:
    def __init__(self):
        # Inicializa el cliente que se comunica con la API externa
        self.client = PokeClient()

    # Función para obtener los datos de un Pokémon por su ID
    async def get_pokemon_data(self, pokemon_id: int) -> PokemonResponseDTO:
        # Cargar configuraciones desde las variables de entorno
        settings = Settings()

        # Construir la URL de la API externa usando el ID
        url = settings.API_URL.format(id=pokemon_id)

        # Realizar la petición a la API externa
        response = await self.client.get_pokemon_id(pokemon_id)

        # Validar que la respuesta sea correcta
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Pokemon no encontrado"
            )

        # Convertir la respuesta a JSON
        data = response.json()

        # Validar que existan datos
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Datos del Pokemon no encontrados"
            )
    
        # Crear el objeto de respuesta usando el DTO
        pokemon_data = PokemonResponseDTO(
            id=data["id"],
            name=data["name"],
            height=data["height"],
            weight=data["weight"],
            image_url=settings.IMG_URL.format(id=pokemon_id)
        )

        # Retornar la información del Pokémon
        return pokemon_data

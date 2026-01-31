from fastapi import APIRouter
from services.poke_services import PokeServices
from DTOs.poke_dto import PokemonResponseDTO

# Crear el router para los endpoints de Pokémon
router = APIRouter()

# Crear instancia del servicio de Pokémon
service = PokeServices()

# Endpoint para obtener un Pokémon por su ID
@router.get("/{pokemon_id}", response_model=PokemonResponseDTO)
async def get_pokemon(pokemon_id: int):
    # Llamar al servicio para obtener los datos del Pokémon
    return await service.get_pokemon_data(pokemon_id)

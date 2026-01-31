from pydantic import BaseModel, Field

# Modelo de datos para la respuesta del Pokémon
class PokemonResponseDTO(BaseModel):
    # Identificador único del Pokémon
    id: int = Field(..., description="ID del Pokemon")
    
    # Nombre del Pokémon
    name: str
    
    # Altura del Pokémon
    height: int
    
    # Peso del Pokémon
    weight: int
    
    # URL de la imagen oficial del Pokémon
    image_url: str

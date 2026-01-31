from fastapi import FastAPI
from controllers.poke_controller import router

# Crear la aplicación FastAPI
app = FastAPI()

# Agregar las rutas del módulo Pokémon
app.include_router(router, prefix="/pokemon", tags=["Pokemon"])

# Ruta principal para comprobar que la API funciona
@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokemon API!"}

# Ejecutar la aplicación
if __name__ == "__main__":    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
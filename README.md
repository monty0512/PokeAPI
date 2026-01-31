# 📘 Pokémon API – Documentación del Contrato

## 📌 Descripción general

### ¿Qué hace la API?
La Pokémon API es un servicio REST desarrollado con FastAPI que permite consultar información básica de Pokémon a partir de su identificador numérico (ID). La API funciona como una capa intermedia que consume datos de una fuente externa y los expone de forma estructurada y simplificada.

### ¿Qué información devuelve?
La API retorna información relevante de cada Pokémon, incluyendo su identificador, nombre, altura, peso y la URL de su imagen oficial.

### ¿Para qué sirve?
Esta API puede ser utilizada en proyectos académicos, aplicaciones educativas, interfaces gráficas de escritorio y como ejemplo práctico del consumo de servicios REST bajo una arquitectura cliente–servidor.

---

## 🔗 Endpoints disponibles

### 🔹 Obtener Pokémon por ID

📍 URL del endpoint  
GET /pokemon/{pokemon_id}

📌 Método HTTP  
GET

📌 Parámetros requeridos  

- pokemon_id (int): Identificador numérico del Pokémon

---

### 📤 Ejemplo de petición

GET http://127.0.0.1:8000/pokemon/25

---

## 📥 Respuestas

### ✅ Respuesta exitosa (200 OK)

{
  "id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
}

---

### 📌 Descripción de los campos

- id: Identificador único del Pokémon  
- name: Nombre del Pokémon  
- height: Altura del Pokémon  
- weight: Peso del Pokémon  
- image_url: URL de la imagen oficial del Pokémon  

---

## ⚠️ Manejo de errores

### ❌ Error 404 – Pokémon no encontrado

Ejemplo de respuesta:
{
  "detail": "Pokemon no encontrado"
}

Explicación:  
Este error se presenta cuando el identificador ingresado no corresponde a un Pokémon existente o cuando el recurso no está disponible en la fuente de datos externa.

---

### ❌ Error 500 – Error interno del servidor

Ejemplo de respuesta:
{
  "detail": "Error interno del servidor"
}

Explicación:  
Este error indica un fallo interno de la aplicación, generalmente asociado a problemas de comunicación con la API externa o errores en el procesamiento de la respuesta.

---

## 🛠️ Tecnologías utilizadas

- FastAPI – Framework para el desarrollo de APIs REST  
- HTTPX – Cliente HTTP asíncrono  
- Pydantic – Validación y modelado de datos  
- Uvicorn – Servidor ASGI  
- Tkinter – Cliente gráfico de escritorio  

---

## ▶️ Ejecución del proyecto

1. Ejecutar el backend  
uvicorn main:app --host 127.0.0.1 --port 8000

2. Acceder a la documentación interactiva  
http://127.0.0.1:8000/docs

3. Ejecutar el cliente gráfico  
python ui_pokemon.py

---

## 📎 Nota técnica
La API adapta la información obtenida de una fuente externa a un formato propio, garantizando encapsulación del servicio y separación de responsabilidades entre backend y frontend.

---

## 👨‍💻 Autor
Proyecto desarrollado con fines académicos como parte del proceso de formación en consumo y documentación de APIs REST.


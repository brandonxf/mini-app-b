from pathlib import Path

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import servicios

app = FastAPI(title="Trivia de cultura general")
plantillas = Jinja2Templates(directory=Path(__file__).parent / "templates")


class Respuesta(BaseModel):
    id: int
    opcion: int = Field(ge=0, le=3)


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request):
    return plantillas.TemplateResponse(request, "index.html")


@app.get("/api/preguntas")
def obtener_preguntas(cantidad: int = Query(5, ge=1, le=5)):
    return servicios.listar_preguntas(cantidad)


@app.post("/api/responder")
def responder(respuesta: Respuesta):
    try:
        return servicios.evaluar_respuesta(respuesta.id, respuesta.opcion)
    except servicios.PreguntaNoEncontrada:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada") from None

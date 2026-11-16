"""Lógica y datos en memoria de la trivia. No depende de FastAPI."""

PREGUNTAS = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Cuál es la capital de Francia?",
        "opciones": ["Madrid", "Roma", "París", "Berlín"],
        "correcta": 2,
    },
    {
        "id": 3,
        "texto": "¿Quién escribió «Don Quijote de la Mancha»?",
        "opciones": [
            "Miguel de Cervantes",
            "Gabriel García Márquez",
            "Lope de Vega",
            "Jorge Luis Borges",
        ],
        "correcta": 0,
    },
    {
        "id": 4,
        "texto": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Atlántico", "Índico", "Ártico", "Pacífico"],
        "correcta": 3,
    },
    {
        "id": 5,
        "texto": "¿Cuántos continentes hay en la clasificación más común?",
        "opciones": ["Cinco", "Seis", "Siete", "Ocho"],
        "correcta": 2,
    },
]


class PreguntaNoEncontrada(Exception):
    """El id solicitado no corresponde a ninguna pregunta."""


def listar_preguntas(cantidad: int = 5) -> list[dict]:
    """Devuelve las primeras `cantidad` preguntas sin la respuesta correcta."""
    return [
        {"id": p["id"], "texto": p["texto"], "opciones": list(p["opciones"])}
        for p in PREGUNTAS[:cantidad]
    ]


def evaluar_respuesta(id_pregunta: int, opcion: int) -> dict:
    """Indica si la opción es correcta y cuál era la respuesta correcta."""
    for pregunta in PREGUNTAS:
        if pregunta["id"] == id_pregunta:
            return {
                "correcta": opcion == pregunta["correcta"],
                "respuesta_correcta": pregunta["correcta"],
            }
    raise PreguntaNoEncontrada(id_pregunta)

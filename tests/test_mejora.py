import pytest
from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


@pytest.mark.parametrize("cantidad", [1, 2, 3, 4, 5])
def test_cantidad_valida(cantidad):
    respuesta = cliente.get("/api/preguntas", params={"cantidad": cantidad})
    assert respuesta.status_code == 200
    preguntas = respuesta.json()
    assert len(preguntas) == cantidad
    for pregunta in preguntas:
        assert set(pregunta) == {"id", "texto", "opciones"}
        assert len(pregunta["opciones"]) == 4


def test_sin_parametro_devuelve_cinco():
    assert len(cliente.get("/api/preguntas").json()) == 5


@pytest.mark.parametrize("cantidad", ["0", "6", "9", "-1", "abc"])
def test_cantidad_invalida(cantidad):
    respuesta = cliente.get("/api/preguntas", params={"cantidad": cantidad})
    assert respuesta.status_code == 422


def test_cantidad_dos_son_las_primeras_dos():
    todas = cliente.get("/api/preguntas").json()
    dos = cliente.get("/api/preguntas", params={"cantidad": 2}).json()
    assert dos == todas[:2]
    assert dos[0]["id"] != dos[1]["id"]

## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.

## Objetivo
Agregar a la trivia el parámetro opcional cantidad en GET /api/preguntas. Acepta un entero entre 1 y 5 y devuelve solo esa cantidad de preguntas; sin el parámetro devuelve 5, y con un valor fuera del rango responde con el código 422. La página principal también debe permitir elegir cuántas preguntas se juegan (de 1 a 5) antes de empezar, y usar ese valor al pedir las preguntas.

## Contexto
Lee AGENTS.md, app/main.py, app/servicios.py, app/templates/index.html y tests/test_aceptacion.py. Las pruebas de aceptación actuales deben seguir pasando sin cambios.

## Restricciones
- No modifiques tests/test_aceptacion.py.
- Escribe la prueba nueva en tests/test_mejora.py. Debe comprobar el contenido de la respuesta (cantidad de preguntas y que no se revele la respuesta correcta), no solo el código de estado.
- Usa solo las dependencias de requirements.txt.
- Las rutas van en app/main.py y la lógica en app/servicios.py, sin importar FastAPI en servicios.
- La página usa HTML, CSS y JavaScript sin librerías externas.
- No hagas commit ni push.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a modificar o crear y espera mi aprobación. Al terminar, resume en una línea qué cambió en cada archivo.

## Ejemplo
GET /api/preguntas?cantidad=2 devuelve una lista con 2 preguntas, cada una con id, texto y opciones.

GET /api/preguntas devuelve 5 preguntas.

GET /api/preguntas?cantidad=9 responde con el código 422.

## Criterio de éxito
python -m pytest -v pasa todas las pruebas, las de aceptación y las de la mejora, y ruff check . no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema.

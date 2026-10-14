# Pythonscripts

Colección de utilidades personales en Python. El usuario va pidiendo scripts nuevos según se le ocurren.

## Convenciones

- Cada utilidad es un único archivo independiente en `scripts/`, con nombre en `snake_case` y en español.
- Partir de `scripts/_plantilla.py`: docstring con descripción y ejemplos, `argparse` para los argumentos, función `main()` que devuelve el código de salida.
- Preferir la librería estándar. Si hace falta una dependencia externa, añadirla a `requirements.txt` indicando qué script la usa.
- Mensajes, ayuda y comentarios en español.
- Al añadir un script, añadir también su fila en la tabla "Scripts" del `README.md`.
- Probar el script (al menos `--help` y un caso real) antes de hacer commit.

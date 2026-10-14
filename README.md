# Pythonscripts

Colección de scripts de Python con utilidades personales. Cada script es independiente y se ejecuta desde la línea de comandos.

## Uso

```bash
# (opcional) crear un entorno virtual e instalar dependencias
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt

# ejecutar un script
python scripts/<nombre>.py --help
```

## Scripts

| Script | Descripción |
| ------ | ----------- |
| _(todavía ninguno)_ | |

## Añadir un script nuevo

1. Copia `scripts/_plantilla.py` a `scripts/<nombre>.py`.
2. Rellena el docstring, los argumentos y la lógica.
3. Si necesita librerías externas, añádelas a `requirements.txt`.
4. Añade una fila a la tabla de arriba.

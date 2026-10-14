#!/usr/bin/env python3
"""Descripción breve de lo que hace el script.

Ejemplos:
    python scripts/nombre.py entrada.txt
    python scripts/nombre.py entrada.txt --verbose
"""

import argparse
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("entrada", help="Argumento de ejemplo")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra más información")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.verbose:
        print(f"Procesando {args.entrada}...", file=sys.stderr)
    # TODO: lógica del script
    return 0


if __name__ == "__main__":
    sys.exit(main())

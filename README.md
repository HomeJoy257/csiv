# FLY2VANS Landing

Página estática (HTML + CSS) para presentar FLY2VANS.

## Si no te abre en el navegador (solución rápida)

Ejecuta este comando dentro de la carpeta del proyecto:

```bash
python3 start-local.py
```

Ese script:
- levanta un servidor local,
- busca otro puerto si `4173` está ocupado,
- e intenta abrir automáticamente el navegador.

## Opciones para abrir la web

### Linux / macOS
```bash
./run-local.sh
```
Después abre:
- `http://127.0.0.1:4173`
- `http://localhost:4173`

### Windows
Haz doble clic en `run-local.bat` o ejecuta:
```bat
python -m http.server 4173
```
Y abre:
- `http://127.0.0.1:4173`

## Problemas típicos

- **Estás en otra carpeta**: entra en la carpeta del proyecto antes de ejecutar comandos.
- **Puerto ocupado**: usa `python3 start-local.py` (elige uno libre automáticamente).
- **Abres `index.html` con `file://`**: mejor usa servidor local para evitar bloqueos del navegador.

## Estructura

- `index.html`: contenido de la landing
- `styles.css`: estilos de la landing
- `start-local.py`: servidor local con detección de puerto
- `run-local.sh`: arranque rápido en Linux/macOS
- `run-local.bat`: arranque rápido en Windows

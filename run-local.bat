@echo off
cd /d %~dp0
echo Iniciando servidor en http://127.0.0.1:4173
python -m http.server 4173

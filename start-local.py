#!/usr/bin/env python3
import http.server
import os
import socket
import socketserver
import webbrowser

HOST = "127.0.0.1"
DEFAULT_PORT = 4173


def find_free_port(start_port: int) -> int:
    port = start_port
    while port < start_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if sock.connect_ex((HOST, port)) != 0:
                return port
        port += 1
    raise RuntimeError("No se encontró un puerto libre entre 4173 y 4222")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_free_port(DEFAULT_PORT)
    url = f"http://{HOST}:{port}"

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((HOST, port), handler) as httpd:
        print(f"Servidor iniciado en {url}")
        print("Pulsa Ctrl+C para cerrar")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido")

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import urllib.request

API = "https://guiafacilmaua.onrender.com"
CAMINHOS = ("/services", "/support", "/steps/", "/chatbot/")


class Pagina(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(CAMINHOS):
            self.encaminhar()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/chatbot/"):
            self.encaminhar()
        else:
            self.send_error(404)

    def encaminhar(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        corpo = self.rfile.read(tamanho) if tamanho else None
        pedido = urllib.request.Request(API + self.path, data=corpo, method=self.command)
        if corpo:
            pedido.add_header("Content-Type", self.headers.get("Content-Type", "application/json"))
        try:
            with urllib.request.urlopen(pedido, timeout=70) as resposta:
                dados = resposta.read()
                self.send_response(resposta.status)
                self.send_header("Content-Type", resposta.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(dados)))
                self.end_headers()
                self.wfile.write(dados)
        except Exception:
            self.send_error(502)


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8765), Pagina).serve_forever()

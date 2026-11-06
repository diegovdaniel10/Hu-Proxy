import http.server
import socketserver
import urllib.request
import urllib.error
import os

# Render assigns a dynamic port via environment variables, default to 8080 for local testing
PORT = int(os.environ.get("PORT", 8080))

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Proxying request for: {self.path}")
        try:
            req = urllib.request.Request(
                self.path,
                headers=dict(self.headers)
            )
            
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for key, value in response.headers.items():
                    if key.lower() in ['transfer-encoding', 'connection']:
                        continue
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
                
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Proxy Error: {str(e)}".encode('utf-8'))

    def do_POST(self):
        self.do_GET()

if __name__ == "__main__":
    # Bind to 0.0.0.0 so Render can receive external traffic
    with socketserver.TCPServer(("0.0.0.0", PORT), ProxyHandler) as httpd:
        print(f"Hu Nao, your HTTP proxy is running on port {PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down proxy server.")
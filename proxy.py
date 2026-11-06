import http.server
import socketserver
import urllib.request
import urllib.error
import os
from urllib.parse import parse_qs, urlparse

PORT = int(os.environ.get("PORT", 8080))

class WebProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # If the user visits the home page, show a search bar
        if parsed_url.path == "/" or not query_params.get("url"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <html>
                <head><title>Hu-Proxy</title></head>
                <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #1e1e1e; color: white;">
                    <h2>Hu-Proxy Web Portal</h2>
                    <form action="/" method="get">
                        <input type="text" name="url" placeholder="https://example.com" style="width: 300px; padding: 10px; font-size: 16px;">
                        <button type="submit" style="padding: 10px 20px; font-size: 16px;">Go</button>
                    </form>
                </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            return

        # Otherwise, fetch the requested URL
        target_url = query_params.get("url")[0]
        if not target_url.startswith("http"):
            target_url = "https://" + target_url

        try:
            req = urllib.request.Request(target_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for key, value in response.headers.items():
                    if key.lower() in ['transfer-encoding', 'connection', 'content-security-type']:
                        continue
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Proxy Error: {str(e)}".encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), WebProxyHandler) as httpd:
        print(f"Hu Nao, Web Proxy running on port {PORT}...")
        httpd.serve_forever()
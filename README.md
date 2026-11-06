# Hu-Proxy
# Hu-Proxy 🚀

A lightweight, simple HTTP proxy server written in Python using only the standard library. Perfect for educational purposes, lightweight traffic routing, or understanding how HTTP proxies work under the hood.

## Features

- **Zero External Dependencies:** Built entirely using Python's built-in `http.server` and `urllib` modules.
- **Method Support:** Handles standard `GET` and `POST` requests.
- **Easy to Setup:** Get a working proxy running in seconds.

## Prerequisites

Make sure you have **Python 3** installed on your system. You can check by running:
\`\`\`bash
python --version
\`\`\`

## Getting Started

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/diegovdaniel10/Hu-Proxy.git
   cd Hu-Proxy
   \`\`\`

2. **Run the proxy script:**
   \`\`\`bash
   python proxy.py
   \`\`\`

   By default, the proxy will start running on `http://localhost:8080`.

## Usage

You can configure your web browser, system network settings, or command-line tools (like `curl`) to route traffic through `http://localhost:8080`.

Example using `curl`:
\`\`\`bash
curl -x http://localhost:8080 http://example.com
\`\`\`

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/diegovdaniel10/Hu-Proxy/issues).

## License

This project is open-source and available under the [MIT License](LICENSE).

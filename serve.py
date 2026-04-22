#!/usr/bin/env python3
"""
Simple HTTP server to serve the Breakout game
Run with: python3 serve.py
Then visit: http://localhost:8000/breakout/
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Set the port
PORT = 8000

# Change to the games directory
games_dir = Path(__file__).parent
os.chdir(games_dir)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[SERVER] {self.address_string()} - {format % args}")

def main():
    handler = MyHTTPRequestHandler

    try:
        # Bind to all interfaces (0.0.0.0) for better ngrok compatibility
        with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
            print(f"🎮 Breakout Game Server")
            print(f"📍 Serving at: http://localhost:{PORT}")
            print(f"🎯 Game URL: http://localhost:{PORT}/breakout/")
            print(f"📁 Serving from: {games_dir}")
            print(f"🛑 Press Ctrl+C to stop")
            print("-" * 50)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use")
            print("Try a different port or stop the other server")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
import os
import sys
from http.server import BaseHTTPRequestHandler

# Add the project root to sys.path so app.py and local assets can be imported/read
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Ensure Streamlit runs in headless mode when app.py is evaluated
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

# Import app.py without modifying it - keeping it as the sole source of truth
import app

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the generated Google Stitch Version 1 HTML application
        content = app.html_content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_HEAD(self):
        content = app.html_content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()

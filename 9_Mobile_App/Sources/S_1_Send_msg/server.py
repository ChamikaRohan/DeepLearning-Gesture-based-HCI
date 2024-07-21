#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import json
from pyngrok import ngrok

# Set ngrok auth token
ngrok.set_auth_token("2jNPEbrb7BPOle1mmLDLqQfg4uO_6B3tjFBLRekfxmhFvtgjn")

class JSONRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Set response headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Read content length
        content_length = int(self.headers['Content-Length'])

        # Read and decode JSON data received
        post_data = self.rfile.read(content_length)
        json_data = json.loads(post_data.decode('utf-8'))

        # Log the received data
        logging.info(f"Received JSON data: {json_data}")

        # Prepare response JSON
        response_data = {
            "status": "success",
            "message": "Data received successfully."
        }

        # Send response back to the client
        self.wfile.write(json.dumps(response_data).encode('utf-8'))


def run_server():
    logging.basicConfig(level=logging.INFO)
    server = HTTPServer(("localhost", 8080), JSONRequestHandler)

    # Start ngrok tunnel
    public_url = ngrok.connect(8080)
    logging.info(f"ngrok tunnel \"{public_url}\" -> \"http://localhost:8080\"")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        ngrok.disconnect(public_url)
        ngrok.kill()
        logging.info("Server stopped.")


if __name__ == "__main__":
    run_server()

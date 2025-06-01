import os
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask in Docker!"

@app.after_request
def set_security_headers(response):
    """Add security headers to each response"""
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Enable XSS protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    # HTTP Strict Transport Security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 8080))
    # Disable debug mode in production
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(host='0.0.0.0', port=port, debug=debug)
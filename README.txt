Custom String Hash Project

Project Overview

Custom String Hash is a web-based application that demonstrates the
fundamentals of hashing algorithms by implementing a custom hash
function and comparing it with the standard SHA-256 algorithm. The
project provides an interactive interface for users to experiment with
different inputs and observe how hash functions work.

Live Application: https://custom-string-hash.onrender.com

Project Structure

custom-string-hash/ ├── app.py # Main Flask application ├──
custom_hash.py # Custom hash algorithm implementation ├──
requirements.txt # Python dependencies ├── render.yaml # Render
deployment configuration └── templates/ └── index.html # Web interface
template

Algorithm Implementation

Core Features

-   Character Manipulation: Converts input characters to ASCII values
    with position-dependent transformations
-   Modular Arithmetic: Uses prime number operations for mixing hash
    values
-   Fixed-Length Output: Produces consistent 32-character hexadecimal
    output
-   Avalanche Effect: Small input changes create significantly different
    hash outputs

Technical Details

-   Input Handling: Processes any string input, including empty strings
-   Position-Dependent Processing: Each character’s transformation
    depends on its position in the input
-   Bit Operations: Implements circular bit shifting and XOR operations
-   Compression: Uses non-linear byte selection for fixed-length output

Web Interface Features

User Experience

-   Clean, responsive web design
-   Real-time hash computation
-   Side-by-side comparison with SHA-256
-   Visual demonstration of hashing principles

Technical Implementation

-   Flask-based web application
-   RESTful API endpoints
-   Jinja2 templating for dynamic content
-   Responsive CSS styling

Deployment

Local Development

Install dependencies: pip install -r requirements.txt

Run development server: python app.py

Cloud Deployment (Render)

-   Automated deployment via connected GitHub repository
-   Configuration through render.yaml
-   Gunicorn WSGI server for production

Educational Value

This project demonstrates: - Fundamental hashing principles and
algorithms - The importance of avalanche effect in hash functions - How
small input changes create significantly different outputs - Differences
between custom and cryptographic hash functions

Technology Stack

-   Backend: Python 3.10+, Flask
-   Frontend: HTML5, CSS3, Jinja2 templates
-   Deployment: Render cloud platform
-   WSGI Server: Gunicorn

Key Features

1.  Custom Hash Algorithm: Implementation of a novel hashing technique
2.  Comparison Tool: Side-by-side analysis with SHA-256
3.  Educational Interface: Clear explanations of hashing concepts
4.  Responsive Design: Works on desktop and mobile devices
5.  Cloud Ready: Easy deployment to Render platform

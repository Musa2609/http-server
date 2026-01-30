# HTTP Server from Scratch (Python)

A basic HTTP server built from scratch using Python sockets to understand how HTTP works at a low level without using any web frameworks.

## Features
- Listens on localhost:8080
- Handles HTTP GET requests
- Parses HTTP request lines manually
- Implements basic routing
- Returns HTML, JSON, and plain-text responses
- Uses proper HTTP status codes

## Routes
- `/` → HTML response
- `/health` → JSON response
- Any other route → 404 Not Found

## Tech Stack
- Python
- Sockets
- HTTP/1.1

## How to Run
```bash
python server.py


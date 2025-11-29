# Flask EC2 Demo

A simple Flask application with basic arithmetic operations, deployed to AWS EC2 using GitHub Actions.

## Features

- **Hello World**: Basic endpoint at `/`
- **Addition**: `/add?a=5&b=3` or POST with JSON `{"a": 5, "b": 3}`
- **Multiplication**: `/multiply?a=4&b=7` or POST with JSON `{"a": 4, "b": 7}`

## Local Setup

1. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## API Endpoints

### GET /
Returns "Hello World!"

### GET/POST /add
Add two numbers.
- GET: `/add?a=5&b=3`
- POST: `{"a": 5, "b": 3}`

### GET/POST /multiply
Multiply two numbers.
- GET: `/multiply?a=4&b=7`
- POST: `{"a": 4, "b": 7}`

## Deployment

This application is automatically deployed to AWS EC2 using GitHub Actions on every push to the main branch.

# Alphabet Checker API

This is a simple RESTful API built using Flask that checks if a given string contains all 26 letters of the English alphabet.

## Features
- Accepts a string input via a POST request.
- Returns `true` if the string contains all letters of the alphabet, otherwise `false`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alphabet-checker-api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd alphabet-checker-api
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask server locally:
```bash
python app.py
```

The API will be available at `http://localhost:5000`.

## API Usage

### Endpoint: `/check-alphabet` (POST)

#### Request:
```json
{
  "input_string": "The quick brown fox jumps over the lazy dog"
}
```

#### Response:
```json
{
  "contains_all_letters": true
}
```

## Testing

Use Postman or `curl` to test the API.

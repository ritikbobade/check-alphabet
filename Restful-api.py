from flask import Flask, request, jsonify

app = Flask(__name__)

def contains_all_letters(input_string):
    found_letters = set()
    for char in input_string.lower():
        if 'a' <= char <= 'z':
            found_letters.add(char)
        if len(found_letters) == 26:
            return True
    return False

@app.route('/check-alphabet', methods=['POST'])
def check_alphabet():
    data = request.json
    
    if 'input_string' not in data:
        return jsonify({'error': 'input_string key is required'}), 400
    
    input_string = data['input_string']
    result = contains_all_letters(input_string)
    
    return jsonify({'contains_all_letters': result})

if __name__ == '__main__':
    app.run(debug=True)

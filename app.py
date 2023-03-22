from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return display_flashcards('hex_questions')

@app.route('/<filename>')
def display_flashcards(filename):
    try:
        with open(f'{filename}.json', 'r') as file:
            cards = json.load(file)
    except FileNotFoundError:
        return render_template('index.html', cards=[{'404 File not found. Head to homepage 127.0.0.1:5000': "404"}])
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)


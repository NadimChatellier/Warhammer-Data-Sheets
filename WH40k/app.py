# app.py

from flask import Flask, render_template

app = Flask(__name__)
#runs the webpage lol
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    nameValue = "Bob"
    return render_template('index.html', name=nameValue)

app.run(debug=True, port=5000)
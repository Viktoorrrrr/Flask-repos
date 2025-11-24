from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = """
        <!doctype html>
        <html>
        <head>
            <title>My styled page</title>
            <link rel="stylesheet" type="text/css" href="/FLASK-REPOS/lesson5.py/static/css/style.css">
        </head>
        <body>
            <h1>Welcome to my stylish page</h2>
            <p>this should look nice</p>
            <p>all made with flask</p>
            <img src="/FLASK-REPOS/lesson5.py/static/images/Flask_logo.svg" alt="Flask logo">
        </body>
        </html>
    """

    return html
app.run(debug=True, port=5000)
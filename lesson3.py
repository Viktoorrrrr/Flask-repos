from flask import Flask
from datetime import datetime

#create the flask app
app = Flask(__name__)

#homepage route
@app.route("/")
def home():

    #get now and format as year-month-day Hour:minute:second
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #set up pages HTML
    html = f"""
        <!doctype html>
        <html>
        <head>
            <title>Clock</title>
        </head>
        <body>
            <h1>Welcome to my clock</h1>
            <p>The current date is {today}</p?
        </body>
        </html>
    """
    #return the HTML
    return html

app.run(debug=True, port=5000)
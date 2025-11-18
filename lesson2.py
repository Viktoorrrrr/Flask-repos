from flask import Flask

#create web host app
app = Flask(__name__)

# this route is for our home page
@app.route('/')
def home():
    return 'Hello world'
# start the web app
app.run(debug=True, port=5000)

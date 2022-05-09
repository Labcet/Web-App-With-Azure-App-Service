from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>My first Web App using Azure App Service!</h1><br><h1>Ernesto Zhildeer Chura Flores</h1></body></html>\n"

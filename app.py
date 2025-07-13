from flask import Flask
app = Flask (__name__)
@app.route("/info")
def flaskinfo():
    return "this is a flask file made in app.py "
app.run()
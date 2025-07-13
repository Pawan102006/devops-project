from flask import Flask
app = Flask (__name__)
@app.route("/")
def flaskinfo():
    return "this is a flask file made in app.pyzgxxxfdnhcyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh "
if __name__=="__main__":
    app.run(host="0.0.0.0" , port="5000")
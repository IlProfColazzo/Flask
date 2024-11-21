from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/francesco")
def hello_francesco():
    str = "Ciao a tutti"
    return "<p>"+str+"</p>"

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

#creare una welcome page, una about us page e una contact page.
#Tre route differenti
#All'interno delle tre pagine inserite una navbar (con i tre link.
#Attenzione i link non devono portare da nessuna parte

app.run(debug=True)
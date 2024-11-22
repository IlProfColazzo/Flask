from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def welcome():
    nomi = ["Andrea", "Mario", "Ettore", "Luigi"]
    return render_template("welcome.html",titolo="Home page", nome = random.choice(nomi))

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)
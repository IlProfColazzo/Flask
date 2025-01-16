from flask import Flask, render_template, request, redirect, url_for
import random
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'
mysql = MySQL(app)

@app.route("/")
def welcome():
    nomi = ["Andrea", "Mario", "Ettore", "Luigi"]
    return render_template("welcome.html",titolo="Home page", nome = random.choice(nomi))

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",titolo="About")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/nomi")
def nomi():
    nomiLista = ["Andrea", "Mario", "Ettore", "Luigi","Camilla"]
    nomiLista.append("Ciccio")
    #tupla
    nomiTupla = ("Andrea", "Mario", "Ettore", "Luigi","Camilla")
    #le tuple sono immutabili
    #la select che scriveremo tornerà una tupla di tuple dove ogni sottotupla 
    #contiene una tupla
    persone = (("Andrea","Colazzo","09111989",34),("Christian","Montanaro","01012001",18)) 
    return render_template("nomi.html",nomi=persone)


@app.route("/firstSelect")
def firstSelect():
    cursor = mysql.connection.cursor()
    query = '''SELECT ProductID, ProductName, CategoryID FROM products'''
    cursor.execute(query)
    dati = cursor.fetchall() #torna il risultato della query
    #fetchall torna una tupla di tuple
    print(dati)
    return render_template("products.html",prodotti=dati)

@app.route("/categoryDescription/<id>")
def details(id):
    cursor = mysql.connection.cursor()
    #query = '''SELECT * FROM categories WHERE CategoryID = ''' + id
    query = '''SELECT * FROM categories WHERE CategoryID = %s'''
    #protezione da sqli
    cursor.execute(query,(id,))
    dati = cursor.fetchall()
    return render_template("details.html",details=dati)

@app.route("/registrati/",methods=["GET","POST"])
def registrati():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        pass
        #logica applicativa
        #controllo che i campi siano presenti
        #posso controllare il tipo
        #controllo le password (lunghezza e confirm)
        #allora faccio una registrazione
        nome = request.form.get("nome","")
        if nome=="":
            print("Campo vuoto o non ricevuto")
        return redirect(url_for('welcome'))
    
app.run(debug=True)
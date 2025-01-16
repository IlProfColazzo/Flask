
    if request.method == 'GET':
        return render_template("register.html")
    else:
        pass
        #logica applicativa
        #controllo che i campi siano presenti
        #posso controllare il tipo
        #controllo le password (lunghezza e confirm)
        #allora faccio una registrazione
    flash("Username already exists", "error")
    return "Ciao" 
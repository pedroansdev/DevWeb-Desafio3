from flask import Flask, render_template

app = Flask("__name__", static_folder="./static", template_folder="./templates")

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'Unes'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemSomos():
    return render_template("quemsomos.html")

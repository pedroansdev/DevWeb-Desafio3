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

@app.route("/quemsomos")
def quemSomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods['POST','GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES(%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'Envio bem sucedido! \nObrigado pelo seu contato :)'

    return render_template("contato.html")


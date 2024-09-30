from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializando a extensão MySQL
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dados')
def get_data():
    # Usando o cursor corretamente
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sua_tabela")  # Altere para o nome da sua tabela
    results = cur.fetchall()
    cur.close()
    return render_template('dados.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from alunos.alunos import aluno_blueprint
from database import db
from flask_migrate import Migrate

app = Flask(__name__)


conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(aluno_blueprint, url_prefix='/aluno')

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)


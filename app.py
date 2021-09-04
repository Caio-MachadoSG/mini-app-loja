from flask import Flask, render_template
from json import load

app = Flask(__name__)


@app.route('/')
def compras():
    with open("static/livros.json", 'r') as jsonLivros:
        recomendacao = load(jsonLivros)
    return render_template("index.html", lista_livros=recomendacao)


if __name__ == '__main__':
    app.run()

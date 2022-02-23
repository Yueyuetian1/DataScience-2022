from flask import Flask
from flask import jsonify
from flask import render_template

from tsp import tsp

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return "<p>Hello, this is my TSP(Traveling Salesman Problem) solution.</p><br/><p>Usage: http://localhost:8080/greedy/10<p>"


@app.route('/greedy/<int:iterations>')
def tsp_greedy(iterations):
    path, distance = tsp(iterations)
    from world_map import get_map_html
    save = 'templates/map.html'
    return get_map_html(path, distance, save)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
    # Jupyter notebook  Debug
    # from werkzeug.serving import run_simple
    # run_simple('localhost', 8080, app)

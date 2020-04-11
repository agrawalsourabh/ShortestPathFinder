from flask import Flask, render_template
from PyFiles import PathFinder
from collections import defaultdict

app = Flask(__name__)
pFinder = PathFinder.PathFinder()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Dijkstra')
def dijkstra():
    path_edge = pFinder.find_dijsktra_path(initial='00', endNode='2040')
    # res = {node: '0' for node in path}
   
    return render_template("home-path.html", result=path_edge, initial='00', endNode='2040')

if __name__ == '__main__':
    app.run(debug=True)
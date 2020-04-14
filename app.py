from flask import Flask, render_template
from PyFiles import PathFinder
from collections import defaultdict

app = Flask(__name__)
pFinder = PathFinder.PathFinder()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Dijkstra/<starting_node>/<ending_node>')
def dijkstra(starting_node, ending_node):
    shortest_path, visited, traverse = pFinder.find_dijsktra_path(initial=starting_node, endNode=ending_node)
    # res = {node: '0' for node in path}
   
    return render_template("home-path.html", shortest_path = shortest_path, distance=len(shortest_path), visited=visited, initial=starting_node, endNode=ending_node, traverse=traverse)

if __name__ == '__main__':
    app.run(debug=True)
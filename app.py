from flask import Flask, render_template
from PyFiles import PathFinder
from collections import defaultdict

from Forms.form import BasicForm

app = Flask(__name__)
# rows = 30 
# columns = 12 


pFinder = PathFinder.PathFinder()

def getDesktopRowsAndCols():
    rows = 18
    columns = 50
    return rows, columns

def getMobileRowsAndCols():
    rows = 30 
    columns = 12
    return rows, columns

is_mobile_view_selected = False

@app.route('/')
def home():
    form = BasicForm()
    if form.validate_on_submit():
        
        rows, columns = getDesktopRowsAndCols()
        pFinder.set_rows(rows=rows)
        pFinder.set_columns(columns=columns)
        pFinder.createGraph()
        return render_template('home_new.html',rows=rows, columns=columns)

    return render_template('index.html')
        
    

    

@app.route('/Dijkstra/<starting_node>/<ending_node>')
def dijkstra(starting_node, ending_node):
    shortest_path, visited, traverse = pFinder.find_dijsktra_path(initial=starting_node, endNode=ending_node)
    # res = {node: '0' for node in path}
    # return traverse

    rows, columns = getDesktopRowsAndCols()
    return render_template("home-path.html", rows=rows, columns=columns, shortest_path = shortest_path, distance=len(shortest_path), visited=visited, initial=starting_node, endNode=ending_node, traverse=traverse)


@app.route('/Astar/<starting_node>/<ending_node>')
def astar(starting_node, ending_node):
    shortest_path, traverse = pFinder.find_astar_path(initial=starting_node, endNode=ending_node)
    # res = {node: '0' for node in path}
    # return traverse
    return render_template("home-path.html", shortest_path = shortest_path, distance=len(shortest_path), visited=None, initial=starting_node, endNode=ending_node, traverse=traverse)


if __name__ == '__main__':
    app.run(debug=True)
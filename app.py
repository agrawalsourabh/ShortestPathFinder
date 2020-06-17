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
    rows = 18 
    columns = 10
    return rows, columns

is_mobile_view_selected = False

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/mobile')
def openMobileView():
    rows, columns = getMobileRowsAndCols()
    pFinder.delete_graph()
    pFinder.set_rows(rows=rows)
    pFinder.set_columns(columns=columns)
    pFinder.createGraph()
    print("Mobile")
    print("Rows")
    print(str(pFinder.get_rows()))
    print("Columns")
    print(str(pFinder.get_columns()))
    return render_template('home_new.html',rows=pFinder.get_rows(), columns=pFinder.get_columns())

@app.route('/desktop')
def openDesktopView():
    rows, columns = getDesktopRowsAndCols()

    pFinder.delete_graph()
    pFinder.set_rows(rows=rows)
    pFinder.set_columns(columns=columns)
    pFinder.createGraph()
    print("Desktop")
    print("Rows")
    print(str(pFinder.get_rows()))
    print("Columns")
    print(str(pFinder.get_columns()))
    return render_template('home_new.html',rows=pFinder.get_rows(), columns=pFinder.get_columns())

@app.route('/Dijkstra/<starting_node>/<ending_node>')
def dijkstra(starting_node, ending_node):
    shortest_path, visited, traverse = pFinder.find_dijsktra_path(initial=starting_node, endNode=ending_node)
    # res = {node: '0' for node in path}
    # return traverse
    print("Dijkstra")
    print("Rows")
    print(str(pFinder.get_rows()))
    print("Columns")
    print(str(pFinder.get_columns()))
    return render_template("home-path.html", rows=pFinder.get_rows(), columns=pFinder.get_columns(), shortest_path = shortest_path, distance=len(shortest_path), visited=visited, initial=starting_node, endNode=ending_node, traverse=traverse)


@app.route('/Astar/<starting_node>/<ending_node>')
def astar(starting_node, ending_node):
    shortest_path, traverse = pFinder.find_astar_path(initial=starting_node, endNode=ending_node)
    # res = {node: '0' for node in path}
    # return traverse
    print("Astar")
    print("Rows")
    print(str(pFinder.get_rows()))
    print("Columns")
    print(str(pFinder.get_columns()))
    return render_template("home-path.html", rows=pFinder.get_rows(), columns=pFinder.get_columns(), shortest_path = shortest_path, distance=len(shortest_path), visited=None, initial=starting_node, endNode=ending_node, traverse=traverse)


if __name__ == '__main__':
    app.run()
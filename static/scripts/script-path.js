$(function() {
    $(".alert-p p").css({
        'color': '#80CBC4'
    });

    $("#navbarDropdown").prop("disabled", true);
});

function visited_cells(visited, shortest_path, initial, endNode) {
    // console.log(JSON.parse(visited))
    var colors = {
        initial_node_color: '#B2DFDB',
        end_node_color: '#00695C',
        visited_node_color: '#64FFDA'
    };
    var jsonData = JSON.parse(visited);
    Object.keys(jsonData).forEach(function(key) {
        var id = "#" + key;
        if (key + "" == initial) {
            $(id).css({
                'background-color': colors.initial_node_color
            });

        } else if (key + "" == endNode) {
            $(id).css({
                'background-color': colors.end_node_color
            });
        } else {
            $(id).css({
                'background-color': colors.visited_node_color
            });
        }
    });

    var i;
    var s_p = JSON.parse(shortest_path);

    Object.keys(s_p).forEach(function(key) {
        var value = s_p[key];
        var id = "#" + value;
        if (value + "" == initial) {
            $(id).css({
                'background-color': '#B2DFDB'
            });

        } else if (value + "" == endNode) {
            $(id).css({
                'background-color': '#00695C'
            });
        } else {
            $(id).css({
                'background-color': '#00BFA5'
            });
        }
    });
}
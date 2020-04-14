var colors = {
    initial_node_color: '#B2DFDB',
    end_node_color: '#00695C',
    visited_node_color: '#64FFDA',
    short_path_node_color: '#00BFA5',
    message_color: '#80CBC4'
};

var window = [];
var trav_flag = false;
let time_delay = 1;

$(function() {


    $("#navbarDropdown").prop("disabled", true);
});

function display_message() {
    $(".alert-p").css({
        'visibility': 'visible'
    });
    $(".alert-p p").css({
        'color': colors.message_color
    });
}

function visited_cells(visited, shortest_path, initial, endNode, traverse) {
    console.log(JSON.parse(visited))
    console.log(traverse)

    console.log("before traverse function - TD: " + time_delay);
    setTimeout(function() {
        highlight_traverse(traverse, initial, endNode);
        console.log("after traverse function - TD: " + time_delay);
        setTimeout(function() {
            highlight_shortest_path(shortest_path, initial, endNode);
            setTimeout(display_message, time_delay);
        }, time_delay);



    }, 0);


    // clearTimeout(time_out);
}

function change_cell_bg_color(id, background_color) {
    $(id).css({
        'background-color': background_color
    });
}

function highlight_shortest_path(shortest_path, initial, endNode) {

    var s_p = JSON.parse(shortest_path);
    console.log("Inside highlight function timeout");
    var i = 1;

    Object.keys(s_p).forEach(function(key) {
        var value = s_p[key];
        var id = "#" + value;
        time_delay = i * 10;
        if (value + "" == initial) {
            $(id).css({
                'background-color': colors.initial_node_color
            });

        } else if (value + "" == endNode) {
            $(id).css({
                'background-color': colors.end_node_color
            });
        } else {
            // change_cell_bg_color(id, colors.short_path_node_color);
            window["reload_timer"] = setTimeout(function() {
                change_cell_bg_color(id, colors.short_path_node_color);
            }, time_delay);
        }
        i = i + 1;
    });
}

function highlight_traverse(traverse, initial, endNode) {

    var s_p = JSON.parse(traverse);
    console.log("Inside highlight function timeout");
    var i = 1;

    Object.keys(s_p).forEach(function(key) {
        var value = s_p[key];
        var id = "#" + value;
        time_delay = 20 * i;

        if (value + "" == initial) {
            $(id).css({
                'background-color': colors.initial_node_color
            });

        } else if (value + "" == endNode) {
            $(id).css({
                'background-color': colors.end_node_color
            });
        } else {
            // change_cell_bg_color(id, colors.short_path_node_color);
            window["reload_timer"] = setTimeout(function() {
                change_cell_bg_color(id, colors.visited_node_color);
            }, time_delay);
        }
        i = i + 1;
        // time_delay = time_delay + 1;


    });


}
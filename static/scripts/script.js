var count = 0;
var colors = {
    initial_node_color: '#B2DFDB',
    end_node_color: '#00695C',
    visited_node_color: '#64FFDA',
    short_path_node_color: '#00BFA5',
    message_color: '#80CBC4'
};
var starting_node = null;
var ending_node = null;

function cellClicked(node) {
    count = count + 1;

    if (count > 2) {
        return;
    } else {
        var id = "td#" + node;

        if (count == 1) { // starting node
            starting_node = "" + node;
            $(id).css({
                'background-color': colors.initial_node_color
            });
        } else { // end node

            ending_node = "" + node;
            $(id).css({
                'background-color': colors.end_node_color
            });
        }
    }
    var url = "/Dijkstra" + "/" + starting_node + "/" + ending_node;
    console.log(url);
    $('#run_btn').attr('data-target', url);
}

function dropdown_item_clicked(btn_text) {

    if (starting_node != null && ending_node != null) {
        $("#run_btn").html("Run " + btn_text).prop("disabled", false);
        var url = "/" + btn_text + "/" + starting_node + "/" + ending_node;
        console.log(url);
        $('#run_btn').attr('data-target', url);
    } else {
        $(".alert-p").css({
            'visibility': 'visible'
        });
        $(".alert-p").css({
            'color': colors.message_color
        });
    }
}


$(function() {
    $("#run_btn").click(function(event) {
        event.preventDefault();
        var url = $(this).data('target');
        location.replace(url);
    });
});
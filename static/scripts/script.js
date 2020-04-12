var count = 0;
var color_code = [{
    start_node: '#B2DFDB',
    end_node: '#00695C'
}];
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
                'background-color': color_code[0].start_node
            });
        } else { // end node

            ending_node = "" + node;
            $(id).css({
                'background-color': color_code[0].end_node
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
        alert("Select nodes first");
    }
}


$(function() {
    $("#run_btn").click(function(event) {
        console.log("btn clicked");
        event.preventDefault();
        var url = $(this).data('target');
        // url = url + "/" + starting_node + "/" + ending_node;
        // console.log(url);
        location.replace(url);
    });
});
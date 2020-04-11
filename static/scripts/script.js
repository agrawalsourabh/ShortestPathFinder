var count = 0;
var color_code = [{
    start_node: '#34eb8f',
    end_node: '#a82d2d'
}];

function cellClicked(i, j) {
    count = count + 1;

    if (count > 2) {
        return;
    } else {
        var id = "td#" + i + j;

        if (count == 1) { // starting node
            $(id).css({
                'background-color': color_code[0].start_node
            });
        } else { // end node
            $(id).css({
                'background-color': color_code[0].end_node
            });
        }
    }
}

function dropdown_item_clicked(btn_text) {
    $("#run_btn").html("Run " + btn_text).prop("disabled", false);
}


// $(function() {
//     $("#run_btn").click(function() {

//     });
// });
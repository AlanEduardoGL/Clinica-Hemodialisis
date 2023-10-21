$(document).ready(function () { // Abre Document Ready

    $("#add_quantity").click(function () {

        var medicine_id = $("#medicine_id").text();
        var quantity = $("#quantity_request").val();

        alert(medicine_id);
        alert(quantity);
        return;

    });

}) // Cierra Document Ready
$(document).ready(function () {

    $(".add_quantity").click(function () {

        var medicine_id = $(this).closest("tr").find(".medicine_id").text();
        var quantity = $(this).closest("tr").find(".quantity_request").val();

        alert(medicine_id);
        alert(quantity);

    });

});

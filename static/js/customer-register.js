$(document).ready(function () {
    $("#submit").on('click', function () {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/v1/customers/register/',
            type: 'POST',
            dataType: 'json',
            data: $("#customer_register_form").serialize(),
            success: function (result) {
                console.log(result);
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
    });
});
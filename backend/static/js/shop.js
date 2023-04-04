var buttons = document.querySelectorAll(".product-card__buy");


for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function (e) {
        e.preventDefault();
        var posting = $.post(e.target.href);
        posting.done(function (data) {
            if (data.status == 'ok') {
                $.notify(data.message, 'success');

            } else {
                $.notify(data.message, 'error');
            }
        })
    });
}

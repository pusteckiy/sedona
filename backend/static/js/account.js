var nicknameForm = $("#nickname-form")
var nicknameFormButton = $("#nickname-form-button")
var codeForm = $("#code-form")
var codeFormButton = $("#code-form-button")
var depositForm = $("#deposit-form")
var depositFormButton = $("#deposit-form-button")
var depositLoading = $("#deposit-loading")


$(function() {
    nicknameForm.submit(function(event) {
        event.preventDefault();
        nicknameFormButton.prop('disabled', true);
        var checkForm = $(this);
        var posting = $.post( checkForm.attr('action'), checkForm.serialize() );
        posting.done(function(data) {
            if(data.status == 'ok') {
                nicknameForm.addClass('d-none')
                codeForm.removeClass('d-none')
            } else {
                $.notify(data.message, 'error');
                nicknameFormButton.prop('disabled', false);
            }
        });
    });

    codeForm.submit(function(event) {
        event.preventDefault();
        codeFormButton.prop('disabled', true);
        var checkForm = $(this);
        var posting = $.post( checkForm.attr('action'), checkForm.serialize() );
        posting.done(function(data) {
            if(data.status == 'ok') {
                codeForm.addClass('d-none')
                $.notify(data.message, 'success');
                location.reload()
            } else {
                $.notify(data.message, 'error');
                codeFormButton.prop('disabled', false);
            }
        });
    });
});


$(function() {
    depositForm.submit(function(event) {
        event.preventDefault();
        depositFormButton.prop('disabled', true);
        depositLoading.removeClass('d-none');
        var checkForm = $(this);
        var posting = $.post( checkForm.attr('action'), checkForm.serialize() );
        posting.done(function(data) {
            console.log(data)
            if(data.status == 'ok') {
                $.notify(data.log, 'success');
                location.reload()
                depositLoading.addClass('d-none')
            } else {
                $.notify(data.log, 'error');
                depositFormButton.prop('disabled', false);
                depositLoading.addClass('d-none')
            }
        });
    });
});
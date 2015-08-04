(function ($) {
    "use strict";
    if ($('#form_send_letter').length <= 0) {
        return;
    }

    // Enable select2 for field "To:"
    $('[name=to]').select2();

    // Setup field with placeholder
    $('.input-area').each(function () {
        var that = $(this);
        this.contentEditable = true;
        if (that.attr('data-placeholder')) {
            that.addClass('js-placeholder');
            that.text(that.attr('data-placeholder'));
        }
    });

    // Setup field with predefined value.
    $('[data-name=doc_title').html($('[name=doc_title]').val());
    $('[data-name=doc_content').html($('[name=doc_content]').val());

    // When editing deletes placeholder
    $('.paper').on('focus', '[data-placeholder]', function () {
        var that = $(this);
        if (that.text() === that.attr('data-placeholder')) {
            that.html("");
        }
        that.removeClass('js-placeholder');
    });
    // When stop editing setup placeholder
    $('.paper').on('blur', '.input-area', function () {
        var that = $(this);
        if ($.trim(that.text()) === '') {
            that.addClass('js-placeholder');
            that.text(that.attr('data-placeholder'));
        }
    });

    // On submit,
    // a) Make sure all fields are filled
    // a) Fill out the hidden inputs
    $('#form_send_letter').submit(function (event) {
        var form = $(this);
        console.log(form.find('.js-placeholder').length > 0);
        if (form.find('.js-placeholder').length > 0) {
            event.preventDefault();
            return;
        }
        $('[data-name]').each(function () {
            var input = $(this);
            var html = input.html();
            var name = input.attr('data-name');
            $('[name=' + name + ']').val(html);
        });
    });
}(jQuery));

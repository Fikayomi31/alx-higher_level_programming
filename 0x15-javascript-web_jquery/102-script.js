$(document).ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click(function () {
        $.get(url + $.parem({ lang: $(INPUT#language_code).val()}), function (dat) {
            $('DIV#hello').html(data.hello)
        })
    })
})
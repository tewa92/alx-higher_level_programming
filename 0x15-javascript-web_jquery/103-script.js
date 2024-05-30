// script that fetches and prints how to say “Hello” depending on
// the language
$(document).ready(function() {
    function fetchTranslation() {
        const langCode = $('#language_code').val();
        if (langCode) {
            $.ajax({
                url: 'https://www.fourtonfish.com/hellosalut/hello/',
                method: 'GET',
                data: { lang: langCode },
                success: function(data) {
                    $('#hello').text(data.hello);
                },
                error: function() {
                    $('#hello').text('Error: Unable to fetch translation.');
                }
            });
        } else {
            $('#hello').text('Please enter a language code.');
        }
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
        if (event.which == 13) { // 13 is the Enter key code
            fetchTranslation();
        }
    });
});

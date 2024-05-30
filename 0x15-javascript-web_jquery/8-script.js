// script that fetches and lists the title for all movies by using this
//URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            const films = data.results;
            films.forEach(film => {
                $('#list_movies').append('<li>' + film.title + '</li>');
            });
        }
    });
});

$.get('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data['results'], function (index, dict) {
    $('#list_movies').append('<li>' + dict['title'] + '</li>');
  });
}, 'json');

$.getJSON('https://swapi.co/api/people/5/?format=json', function (response) {
  $('#character').text(response.name);
});

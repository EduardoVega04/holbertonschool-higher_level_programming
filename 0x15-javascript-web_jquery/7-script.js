$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
    if (data) {         
      $("div#character").text(data["name"]);
    }
  });
});

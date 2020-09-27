$(document).ready(function () {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data, status) {
      if (data) {         
        const list_movies = data["results"];
        const length_list = list_movies.length;
        for (let i = 0; i < length_list; i++) {
            let movie_title = list_movies[i]["title"];
            const content = $("<li></li>").text(movie_title);
            $("ul#list_movies").append(content);
        }
      }
    });
  });
  
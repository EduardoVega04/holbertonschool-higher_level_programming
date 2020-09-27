$(document).ready(function () {
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function (data, status) {
      if (data) {
        const hello = data["hello"];              
        $("div#hello").text(hello);
      }
    });
});

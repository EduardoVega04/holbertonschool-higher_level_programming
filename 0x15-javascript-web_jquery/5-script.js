$(document).ready(function(){
    $("div#add_item").click(function(){
      const content = $("<li></li>").text("Item");
      $("UL.my_list").append(content);
    });
});

$(document).ready(function() {
    $.getJSON("/static/projects/data/faculties.json", function(data){
        
        console.log(data);
        $("h1").html(data.category);

       $("#faculties-list").append("<ul>");
       $.each(data.faculties, function() {
           $("#faculties-list ul").append("<li><img src='" + this.imgUrl + "'><br>" + this.name
           + "</li>");
       });
       $("#faculties-list").append("</ul>");
    });
});
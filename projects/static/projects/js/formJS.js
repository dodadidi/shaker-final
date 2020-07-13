function checkForm(){
    var counter =0;
    $("input[type=checkbox]").each(function (id,element){
        if(element.checked){
            counter++;
        }
    });

    if(counter==0){
        alert("Please choose at least one department");
        return false;
    }
    return true;
   
}
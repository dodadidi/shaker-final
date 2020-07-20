initialize(); 

function initialize() {
    var main_wrapper = document.getElementsByClassName('main_wrapper')[0];
    var rect = document.createElement("div");
    var rectangles =[{title:'Princesses',url:'#',image:'./images/5.png'},
                    {title:'Electric dress',url:'electricDress.html',image:'./images/2.jpg'}];
    
    for(i = 0; i < rectangles.length; i++) {
    var rect_obj = rectangles[i];
    rect = rect.cloneNode();
    rect.classList.add("card");
    rect.setAttribute("id",i);
    var img = document.createElement("img");
    img.classList.add("card-img-top");
    img.classList.add("gallery");
    img.setAttribute("src",rect_obj.image);
    var aTarget = document.createElement("a");
    aTarget.href = rect_obj.url;
    aTarget.append(img);
    var cardBody = document.createElement("a");
    cardBody.href = rect_obj.url;
    cardBody.classList.add("card-body1");
    var cardText = document.createElement("p");
    cardText.classList.add("card-text");
    cardText.innerText=rect_obj.title;
    cardBody.append(cardText);
    rect.append(aTarget);
    rect.append(cardBody);
    main_wrapper.append(rect);    
    }
}

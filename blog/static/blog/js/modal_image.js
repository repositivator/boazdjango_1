// Get the modal
var modal = document.getElementById('myModal');


// Get the image and insert it inside the modal - use its "alt" text as a caption
/*var img = document.getElementById('myImg');*/
var img = document.getElementsByClassName('myImg')[0];
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    modalImg.alt = this.alt;
    captionText.innerHTML = this.alt;
}
var img = document.getElementsByClassName('myImg')[1];
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    modalImg.alt = this.alt;
    captionText.innerHTML = this.alt;
}


var img = document.getElementsByClassName('myImg')[2];
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    modalImg.alt = this.alt;
    captionText.innerHTML = this.alt;
}


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var modal_content = document.getElementsByClassName("modal-content")[0];



// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
modal_content.onclick = function() { 
  modal.style.display = "none";
}
modal.onclick = function() { 
  modal.style.display = "none";
}
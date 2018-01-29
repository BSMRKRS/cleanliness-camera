function show_image(event){
  file_name = event.target.innerHTML;
  document.getElementById('current-image-title').innerHTML = "<p>"+file_name+"</p>";
  document.getElementById('current-image').innerHTML = "<img src='/pictures/" + file_name + "'></img>";
}

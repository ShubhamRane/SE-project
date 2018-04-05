canvas = document.querySelector("canvas");
context = canvas.getContext('2d');




$('#canvas').mousedown(function(e){
  var mouseX = e.pageX;
  var mouseY = e.pageY;
  var rect = canvas.getBoundingClientRect();
  paint = true;
  addClick(mouseX-rect.left, mouseY-rect.top);
  console.log($(this).offset());
  redraw();
});



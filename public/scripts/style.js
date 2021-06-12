function updateTextInsideTemp(val) {
   document.getElementById('textInputInside').value=val +"°C" ; 
 }
 function updateTextOutsideTemp(val) {
  document.getElementById('textInputOutside').value=val+"°C"; 
}

function updateTextPeople(val) {
  document.getElementById('textInputPeople').value=val; 
}

function changeOutputTemperature(val){
 const h4 =  $("#fuzzyOutput")[0]
 const str = val.toFixed(2) +" °C"
  h4.innerHTML = str
}


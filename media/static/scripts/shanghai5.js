function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;
  // While there remain elements to shuffle...
  while (0 !== currentIndex) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
}

function randomizeEventTimeOptions() {
  // shuffle order
  var order = [1, 2, 3];
  order = shuffle(order);
  // record as hidden input
  document.getElementById("eventTempOptionsOrder").value = order.join('');
  // update order
  var i;
  for (i = 0; i < order.length - 1; i++) {
    $( "#tempOption"+order[i] ).after( $( "#tempOption"+order[i+1] ) );
  }
}

$( document ).ready(function() {
  randomizeEventTimeOptions();
});

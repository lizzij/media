function donationWillingSlide() {
  var value=document.getElementById("donationWillingSlider").value;
  var donationWillingAmount = `${value}元`;
  document.getElementById("donationWillingAmount").value=donationWillingAmount;
  var left = 2 + 0.9 * value;
  document.getElementById("donationWillingAmount").style.marginLeft = left + "px";
}

function outdoorTimeSlide() {
  var value=document.getElementById("outdoorTimeSlider").value;
  var hours;
  var minutes;
  if (value >= 1200) {
    document.getElementById("outdoorTimeAmount").value=`大于等于20小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("outdoorTimeAmount").value=time;
  }
  var left = 0 + 0.17 * value;
  document.getElementById("outdoorTimeAmount").style.paddingLeft = left + "px";
}

function exerciseTimeSlide() {
  var value=document.getElementById("exerciseTimeSlider").value;
  var hours;
  var minutes;
  if (value >= 1200) {
    document.getElementById("exerciseTimeAmount").value=`大于等于20小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("exerciseTimeAmount").value=time;
  }
  var left = 0 + 0.17 * value;
  document.getElementById("exerciseTimeAmount").style.paddingLeft = left + "px";
}

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

function randomize() {
  // shuffle order
  var order = [1, 2, 3, 4, 5];
  order = shuffle(order);
  // record as hidden input
  document.getElementById("newsOrder").value = order.join('');
  // update order
  var i;
  for (i = 0; i < order.length - 1; i++) {
    $( "#news"+order[i] ).after( $( "#news"+order[i+1] ) );
  }
}

function randomizeEventLocationOptions() {
  // shuffle order
  var order = [1, 2, 3, 4];
  order = shuffle(order);
  // record as hidden input
  document.getElementById("eventLocationOptionsOrder").value = order.join('');
  // update order
  var i;
  for (i = 0; i < order.length - 1; i++) {
    $( "#locationOption"+order[i] ).after( $( "#locationOption"+order[i+1] ) );
  }
}

$( document ).ready(function() {
  randomizeEventLocationOptions();
  randomize();
});

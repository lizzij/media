function randomizeCheckAQSource() {
  // shuffle order
  var order = [1, 2, 3, 4, 5, 6, 7];
  order = shuffle(order);
  // record as hidden input
  document.getElementById("checkAQSourceOrder").value = order.join('');
  // update order
  var i;
  for (i = 0; i < order.length - 1; i++) {
    $( "#checkSourceOption"+order[i] ).after( $( "#checkSourceOption"+order[i+1] ) );
  }
}
// Page 5 ======================================================================
// validate star question on page 5 => page 6
function validateStar() {
  var alert = document.getElementById("starAlert").innerHTML;
  var numStarLeft = document.getElementById("starLeftCount").innerHTML;
  if ((parseInt(numStarLeft)) > 0) {
    document.getElementById("starAlert").innerHTML = '请用完所有星星！';
    document.getElementById('page5').style='display: flex;flex-direction: column;position: relative; overflow: visible;';
    document.getElementById("clearAllStarsButton").style.display='block';
    return false;
  }
  return true;
}

function updateStarInput(index) {
  document.getElementById("starCountGroup"+index+"Input").value = document.getElementById("starCountGroup"+index).innerHTML;
}

function starCountGroup(index, number) {
  var starLeftCount = document.getElementById("starLeftCount").innerHTML;
  var count = document.getElementById("starCountGroup" + index).innerHTML;
  if (starLeftCount == 0 && number > count) {
    document.getElementById("starAlert").innerHTML = '已用完12个星星！';
  }
  else if (number - count > starLeftCount) {
    document.getElementById("starAlert").innerHTML = '超过剩余星星！';
  }
  else if (number == 1 && count == 0) {
    document.getElementById("starAlert").innerHTML = '';
    document.getElementById("starGroup"+index+"Cover").innerHTML = '<div class="star" onclick="starCountGroup('+index+'1)">&starf;</div>';
    document.getElementById("starCountGroup"+index).innerHTML = '1';
  }
  else if (number == 1 && count == 1) {
    document.getElementById("starAlert").innerHTML = '';
    document.getElementById("starGroup"+index+"Cover").innerHTML = '';
    document.getElementById("starCountGroup"+index).innerHTML = '0';
  }
  else {
    document.getElementById("starAlert").innerHTML = '';
    var star = '';
    var i;
    for (i = 0; i < number; i++) {
      star = star + '<div class="star" onclick="starCountGroup(' + index + ',' + (i+1) + ')">&starf;</div>';
    }
    document.getElementById("starGroup"+index+"Cover").innerHTML = star;
    document.getElementById("starCountGroup"+index).innerHTML = number;
  }
  starLeft();
  updateStarInput(index);
  var pollutionDescription = [
    "严重污染：健康人群运动耐受力降低，有明显强烈症状，提前出现某些疾病。儿童、老年人和病人应当留在室内，避免体力消耗，一般人群应避免户外活动。",
    "重度污染：心脏病和肺病患者症状显著加剧，运动耐受力降低，健康人群普遍出现症状。儿童、老年人和心脏病、肺病患者应停留在室内，停止户外运动，一般人群减少户外运动。",
    "中度污染：进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响。儿童、老年人及心脏病、呼吸系统疾病患者避免长时间、高强度的户外锻练，一般人群适量减少户外运动。",
    "轻度污染：易感人群症状有轻度加剧，健康人群出现刺激症状。儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼。",
    "良：空气质量可接受，但某些污染物可能对极少数异常敏感人群健康有较弱影响。极少数异常敏感人群应减少户外活动。",
    "优：空气质量令人满意，基本无空气污染。各类人群可正常活动。"
  ];
  document.getElementById("groupDescription").innerHTML = pollutionDescription[index-1];
  return false;
}

function clearAllStars() {
  document.getElementById("starAlert").innerHTML = '';
  var starCounts = ["starCountGroup1", "starCountGroup2", "starCountGroup3",
  "starCountGroup4", "starCountGroup5", "starCountGroup6"];
  var starCovers = ["starGroup1Cover", "starGroup2Cover", "starGroup3Cover",
  "starGroup4Cover", "starGroup5Cover", "starGroup6Cover"];
  var i;
  for (i = 0; i < starCounts.length; i++) {
    var starCount = starCounts[i];
    document.getElementById(starCount).innerHTML = '0';
    var starCover = starCovers[i];
    document.getElementById(starCover).innerHTML = '';
  }
  starLeft();
}

function starLeft() {
  var starLeftCount = 12;
  var starLeft = '';
  starLeftCount = starLeftCount
  - document.getElementById("starCountGroup1").innerHTML
  - document.getElementById("starCountGroup2").innerHTML
  - document.getElementById("starCountGroup3").innerHTML
  - document.getElementById("starCountGroup4").innerHTML
  - document.getElementById("starCountGroup5").innerHTML
  - document.getElementById("starCountGroup6").innerHTML;
  var i;
  for (i = 0; i < starLeftCount; i++) {
    starLeft = starLeft + '<div class="star">&starf;</div>';
  }
  document.getElementById("starLeftCount").innerHTML = starLeftCount + "";
  document.getElementById("starLeftContainer").innerHTML = starLeft;
  showClearAllStarsButton();
}

function showClearAllStarsButton() {
  var starLeftCount = document.getElementById("starLeftCount").innerHTML;
  if ((parseInt(starLeftCount)) < 12) {
    document.getElementById("clearAllStarsButton").style.display='block';
  }
  else {
    document.getElementById("clearAllStarsButton").style.display='none';
  }
}

function randomizeEventTempOptions() {
  // shuffle order
  var order = [1, 2, 3, 4];
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
  randomizeEventTempOptions();
});

$( document ).ready(function() {
  randomizeCheckAQSource();
  randomize();
  randomizeEventTempOptions();
});

function outingSlide(index) {
  document.getElementById("outing"+index+"Amount").value=Math.floor(document.getElementById("outing"+index).value/2)*2;
  var value=document.getElementById("outing"+index).value;
  var factorIds = ['outing'+index+'ScaleLabel1', 'outing'+index+'ScaleLabel2', 'outing'+index+'ScaleLabel3',
  'outing'+index+'ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing"+index+"ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing"+index+"ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing"+index+"ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing"+index+"ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing"+index+"ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing"+index+"ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing"+index+"ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing"+index+"ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing"+index+"Amount").style.paddingLeft = left + "px";
}

// Page 6 ======================================================================
function walkathonSlide() {
  var value=document.getElementById("walkathonSlider").value;
  var walkathonAmount = `${value}步`;
  var distance = value * 0.0008;
  var donation = value * 0.002;
  distance = distance.toFixed(2);
  document.getElementById("walkathonAmount").value=walkathonAmount;
  document.getElementById("walkathonDistance").value=`走${value}步（${distance}公里）\n—— 研究人员将代表您向上海联合基金会捐赠${donation}元人民币。`;
  var left = value * 0.0172;
  document.getElementById("walkathonAmount").style.paddingLeft = left + "px";
}

function hideWalkathonSlider() {
  document.getElementById("walkathon").style.display = "none";
}
function showWalkathonSlider() {
  document.getElementById("walkathon").style.display = "block";
}


// Page % ======================================================================
// Get the modal
var modal = document.getElementById('myModal1');

// Get the <span> element that closes the modal
var span = document.getElementById('close1');

modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Page 9 ======================================================================
function dunno(index) {
  var isDunnoChecked = document.getElementById("dunno"+index+"checkbox").checked
  if (isDunnoChecked) {
    document.getElementById("trustSlider"+index).style.display = "none";
  }
  else {
    document.getElementById("trustSlider"+index).style.display = "block";
  }
}

// Page 9 ======================================================================
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
  var order = [1, 2, 3, 4, 5, 6];
  order = shuffle(order);
  // record as hidden input
  document.getElementById("trustOrder").value = order.join('');
  // update order
  var i;
  for (i = 0; i < order.length - 1; i++) {
    $( "#question"+order[i] ).after( $( "#question"+order[i+1] ) );
  }
}

function trustSlide(index) {
  document.getElementById("trust"+index+"Amount").value=Math.floor(document.getElementById("trust"+index).value/2)*2;
  var trust=document.getElementById("trust"+index).value;
  var trustIds = ['trust'+index+'ScaleLabel1', 'trust'+index+'ScaleLabel2', 'trust'+index+'ScaleLabel3',
  'trust'+index+'ScaleLabel4', 'trust'+index+'ScaleLabel5'];
  var selected;
  for (i = 0; i < trustIds.length; i++) {
    notSelected = trustIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';

  }
  if (0 <= trust && trust < 20) {
    document.getElementById("trust"+index+"ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("trust"+index+"ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (20 <= trust && trust < 40) {
    document.getElementById("trust"+index+"ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("trust"+index+"ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (40 <= trust && trust < 60) {
    document.getElementById("trust"+index+"ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("trust"+index+"ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (60 <= trust && trust < 80) {
    document.getElementById("trust"+index+"ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("trust"+index+"ScaleLabel4").style.color = "#4F4F4F";
  }
  else if (80 <= trust && trust <= 100) {
    document.getElementById("trust"+index+"ScaleLabel5").style.fontWeight = 'bold';
    document.getElementById("trust"+index+"ScaleLabel5").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * trust;
  document.getElementById("trust"+index+"Amount").style.paddingLeft = left + "px";
}

// Get the modal ===============================================================
var modal2 = document.getElementById('myModal2');

// Get the <span> element that closes the modal
var span2 = document.getElementById("close2");

modal2.style.display = "block";

// When the user clicks on <span> (x), close the modal
span2.onclick = function() {
  modal2.style.display = "none";
}

// new questions ===============================================================
function outing1Slide() {
  document.getElementById("outing1Amount").value=Math.floor(document.getElementById("outing1").value/2)*2;
  var value=document.getElementById("outing1").value;
  var factorIds = ['outing1ScaleLabel1', 'outing1ScaleLabel2', 'outing1ScaleLabel3',
  'outing1ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing1ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing1ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing1ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing1ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing1Amount").style.paddingLeft = left + "px";
}

function outing2Slide() {
  document.getElementById("outing2Amount").value=Math.floor(document.getElementById("outing2").value/2)*2;
  var value=document.getElementById("outing2").value;
  var factorIds = ['outing2ScaleLabel1', 'outing2ScaleLabel2', 'outing2ScaleLabel3',
  'outing2ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing2ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing2ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing2ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing2ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing2Amount").style.paddingLeft = left + "px";
}

function outing3Slide() {
  document.getElementById("outing3Amount").value=Math.floor(document.getElementById("outing3").value/2)*2;
  var value=document.getElementById("outing3").value;
  var factorIds = ['outing3ScaleLabel1', 'outing3ScaleLabel2', 'outing3ScaleLabel3',
  'outing3ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing3ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing3ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing3ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing3ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing3Amount").style.paddingLeft = left + "px";
}

function outing4Slide() {
  document.getElementById("outing4Amount").value=Math.floor(document.getElementById("outing4").value/2)*2;
  var value=document.getElementById("outing4").value;
  var factorIds = ['outing4ScaleLabel1', 'outing4ScaleLabel2', 'outing4ScaleLabel3',
  'outing4ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing4ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing4ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing4ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing4ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing4Amount").style.paddingLeft = left + "px";
}

function outing5Slide() {
  document.getElementById("outing5Amount").value=Math.floor(document.getElementById("outing5").value/2)*2;
  var value=document.getElementById("outing5").value;
  var factorIds = ['outing5ScaleLabel1', 'outing5ScaleLabel2', 'outing5ScaleLabel3',
  'outing5ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing5ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing5ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing5ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing5ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing5Amount").style.paddingLeft = left + "px";
}


function blueGraySkyAmountSlide() {
  var value=document.getElementById("blueGraySkyAmountSlider").value;
  var blueGraySkyAmount = `${value}`;
  document.getElementById("blueGraySkyAmount").value=blueGraySkyAmount;
  var left = 3 + 2.88 * value;
  document.getElementById("blueGraySkyAmount").style.marginLeft = left + "px";
  document.getElementById("graySky").style.opacity = (100-value)/100;
}


// new ================================================================
function hideNumberOfTimes() {
  document.getElementById("otherHowManyTimes").style.display = "none";
}
function showNumberOfTimes() {
  document.getElementById("otherHowManyTimes").style.display = "block";
}

function hideNumberOfWeatherTimes() {
  document.getElementById("otherHowManyWeatherTimes").style.display = "none";
}
function showNumberOfWeatherTimes() {
  document.getElementById("otherHowManyWeatherTimes").style.display = "block";
}

function validateOneChecked(name) {
  return ($('input[name='+name+']:checked').length == 1);
}

function validateShownAndFilled(formName, name) {

  var display = document.getElementById(formName).style.display;
  var value = document.getElementById(name).value;

  if (display != "none") {
    return (value != null && value != '');
  }
  return true;
}

// =====
function outing1Slide() {
  document.getElementById("outing1Amount").value=Math.floor(document.getElementById("outing1").value/2)*2;
  var value=document.getElementById("outing1").value;
  var factorIds = ['outing1ScaleLabel1', 'outing1ScaleLabel2', 'outing1ScaleLabel3',
  'outing1ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing1ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing1ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing1ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing1ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing1ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing1Amount").style.paddingLeft = left + "px";
}

function outing2Slide() {
  document.getElementById("outing2Amount").value=Math.floor(document.getElementById("outing2").value/2)*2;
  var value=document.getElementById("outing2").value;
  var factorIds = ['outing2ScaleLabel1', 'outing2ScaleLabel2', 'outing2ScaleLabel3',
  'outing2ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing2ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing2ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing2ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing2ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing2ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing2Amount").style.paddingLeft = left + "px";
}

function outing3Slide() {
  document.getElementById("outing3Amount").value=Math.floor(document.getElementById("outing3").value/2)*2;
  var value=document.getElementById("outing3").value;
  var factorIds = ['outing3ScaleLabel1', 'outing3ScaleLabel2', 'outing3ScaleLabel3',
  'outing3ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing3ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing3ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing3ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing3ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing3ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing3Amount").style.paddingLeft = left + "px";
}

function outing4Slide() {
  document.getElementById("outing4Amount").value=Math.floor(document.getElementById("outing4").value/2)*2;
  var value=document.getElementById("outing4").value;
  var factorIds = ['outing4ScaleLabel1', 'outing4ScaleLabel2', 'outing4ScaleLabel3',
  'outing4ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing4ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing4ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing4ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing4ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing4ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing4Amount").style.paddingLeft = left + "px";
}

function outing5Slide() {
  document.getElementById("outing5Amount").value=Math.floor(document.getElementById("outing5").value/2)*2;
  var value=document.getElementById("outing5").value;
  var factorIds = ['outing5ScaleLabel1', 'outing5ScaleLabel2', 'outing5ScaleLabel3',
  'outing5ScaleLabel4'];
  var selected;
  for (i = 0; i < factorIds.length; i++) {
    notSelected = factorIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';
  }
  if (0 <= value && value < 25) {
    document.getElementById("outing5ScaleLabel1").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel1").style.color = "#4F4F4F";
  }
  else if (25 <= value && value < 50) {
    document.getElementById("outing5ScaleLabel2").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel2").style.color = "#4F4F4F";
  }
  else if (50 <= value && value < 75) {
    document.getElementById("outing5ScaleLabel3").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel3").style.color = "#4F4F4F";
  }
  else if (75 <= value && value <= 100) {
    document.getElementById("outing5ScaleLabel4").style.fontWeight = 'bold';
    document.getElementById("outing5ScaleLabel4").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * value;
  document.getElementById("outing5Amount").style.paddingLeft = left + "px";
}

// validate how many times is filled page 8 => 9
function validateHowManyTimesForcedAns() {
  var bothFilled = validateShownAndFilled("otherHowManyTimes", "numberOfTimes")
      && validateShownAndFilled("otherHowManyWeatherTimes", "numberOfWeatherTimes")
  if (!bothFilled) {
    document.getElementById("fillAll").innerHTML='请填写次数';
    return false;
  }
  return true;
}

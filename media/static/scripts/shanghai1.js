// page 1 ======================================================================

function walkathonSlide() {
  var value=document.getElementById("walkathonSlider").value;
  var walkathonAmount = `${value}步`;
  var distance = value * 0.0008;
  var donation = value * 0.002;
  distance = distance.toFixed(2);
  document.getElementById("walkathonAmount").value=walkathonAmount;
  document.getElementById("walkathonDistance").value=`走${value}步（${distance}公里）`;
  var left = value * 0.0172;
  document.getElementById("walkathonAmount").style.paddingLeft = left + "px";
}

function hideWalkathonSlider() {
  document.getElementById("walkathon").style.display = "none";
}
function showWalkathonSlider() {
  document.getElementById("walkathon").style.display = "block";
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

// page 2 ======================================================================
// validate weather star question on page 2 => page3
function validateWeatherStar() {
  var alert = document.getElementById("weatherStarAlert").innerHTML;
  var numStarLeft = document.getElementById("weatherStarLeftCount").innerHTML;
  if ((parseInt(numStarLeft)) > 0) {
    document.getElementById("weatherStarAlert").innerHTML = '请用完所有星星！';
    document.getElementById('page2').style='display: flex;flex-direction: column;position: relative; overflow: visible;';
    document.getElementById("weatherClearAllStarsButton").style.display='block';
    return false;
  }
  return true;
}

function updateInput(index) {
  document.getElementById("weatherStarCountGroup" + index + "Input").value = document.getElementById("weatherStarCountGroup" + index).innerHTML;
}

weatherShowClearAllStarsButton()

function weatherStarCountGroup(index, number) {
  var weatherStarLeftCount = document.getElementById("weatherStarLeftCount").innerHTML;
  var count = document.getElementById("weatherStarCountGroup" + index).innerHTML;
  if (weatherStarLeftCount == 0 && number > count) {
    document.getElementById("weatherStarAlert").innerHTML = '已用完12个星星！';
  }
  else if (number - count > weatherStarLeftCount) {
    document.getElementById("weatherStarAlert").innerHTML = '超过剩余星星！';
  }
  else if (number == 1 && count == 0) {
    document.getElementById("weatherStarAlert").innerHTML = '';
    document.getElementById("weatherStarGroup" + index + "Cover").innerHTML = '<div class="star" onclick="weatherStarCountGroup('+index+',1)">&starf;</div>';
    document.getElementById("weatherStarCountGroup" + index).innerHTML = '1';
  }
  else if (number == 1 && count == 1) {
    document.getElementById("weatherStarAlert").innerHTML = '';
    document.getElementById("weatherStarGroup1Cover").innerHTML = '';
    document.getElementById("weatherStarCountGroup" + index).innerHTML = '0';
  }
  else {
    document.getElementById("weatherStarAlert").innerHTML = '';
    var star = '';
    var i;
    for (i = 0; i < number; i++) {
      star = star + '<div class="star" onclick="weatherStarCountGroup(' + index + ',' + (i+1) + ')">&starf;</div>';
    }
    document.getElementById("weatherStarGroup" + index + "Cover").innerHTML = star;
    document.getElementById("weatherStarCountGroup" + index).innerHTML = number;
  }
  weatherStarLeft();
  updateInput(index);
  return false;
}

function weatherStarLeft() {
  var weatherStarLeftCount = 12;
  var weatherStarLeft = '';
  weatherStarLeftCount = weatherStarLeftCount
  - document.getElementById("weatherStarCountGroup1").innerHTML
  - document.getElementById("weatherStarCountGroup2").innerHTML
  - document.getElementById("weatherStarCountGroup3").innerHTML
  - document.getElementById("weatherStarCountGroup4").innerHTML;
  var i;
  for (i = 0; i < weatherStarLeftCount; i++) {
    weatherStarLeft = weatherStarLeft + '<div class="star">&starf;</div>';
  }
  document.getElementById("weatherStarLeftCount").innerHTML = weatherStarLeftCount + "";
  document.getElementById("weatherStarLeftContainer").innerHTML = weatherStarLeft;
  weatherShowClearAllStarsButton();
}

function weatherShowClearAllStarsButton() {
  var weatherStarLeftCount = document.getElementById("weatherStarLeftCount").innerHTML;
  if ((parseInt(weatherStarLeftCount)) < 12) {
    document.getElementById("weatherClearAllStarsButton").style.display='block';
  }
  else {
    document.getElementById("weatherClearAllStarsButton").style.display='none';
  }
}

function weatherClearAllStars() {
  document.getElementById("weatherStarAlert").innerHTML = '';
  var starCounts = ["weatherStarCountGroup1", "weatherStarCountGroup2", "weatherStarCountGroup3",
  "weatherStarCountGroup4"];
  var starCovers = ["weatherStarGroup1Cover", "weatherStarGroup2Cover", "weatherStarGroup3Cover",
  "weatherStarGroup4Cover"];
  var i;
  for (i = 0; i < starCounts.length; i++) {
    var starCount = starCounts[i];
    document.getElementById(starCount).innerHTML = '0';
    var starCover = starCovers[i];
    document.getElementById(starCover).innerHTML = '';
  }
  weatherStarLeft();
}


// page 3 ======================================================================

// page 4 ======================================================================

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
    "优：空气质量令人满意，基本无空气污染。各类人群可正常活动。",
    "良：空气质量可接受，但某些污染物可能对极少数异常敏感人群健康有较弱影响。极少数异常敏感人群应减少户外活动。",
    "轻度污染：易感人群症状有轻度加剧，健康人群出现刺激症状。儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼。",
    "中度污染：进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响。儿童、老年人及心脏病、呼吸系统疾病患者避免长时间、高强度的户外锻练，一般人群适量减少户外运动。",
    "重度污染：心脏病和肺病患者症状显著加剧，运动耐受力降低，健康人群普遍出现症状。儿童、老年人和心脏病、肺病患者应停留在室内，停止户外运动，一般人群减少户外运动。",
    "严重污染：健康人群运动耐受力降低，有明显强烈症状，提前出现某些疾病。儿童、老年人和病人应当留在室内，避免体力消耗，一般人群应避免户外活动。"
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

// page 5 ======================================================================

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

function dunno(index) {
  var isDunnoChecked = document.getElementById("dunno"+index+"checkbox").checked
  if (isDunnoChecked) {
    document.getElementById("trustSlider"+index).style.display = "none";
  }
  else {
    document.getElementById("trustSlider"+index).style.display = "block";
  }
}

$( document ).ready(function() {
  randomize();
});

// page 6 ======================================================================

function willingnessSlide() {
  document.getElementById("willingnessAmount").value=Math.floor(document.getElementById("willingness").value/2)*2;
  var trust=document.getElementById("willingness").value;
  trust = Math.floor(trust);
  var trustIds = ['willingnessLabel1', 'willingnessLabel2', 'willingnessLabel3',
  'willingnessLabel4', 'willingnessLabel5'];
  var selected;
  for (i = 0; i < trustIds.length; i++) {
    notSelected = trustIds[i];
    document.getElementById(notSelected).style.color = "#979797";
    document.getElementById(notSelected).style.fontWeight = 'normal';

  }
  if (0 <= trust && trust < 20) {
    document.getElementById("willingnessLabel1").style.fontWeight = 'bold';
    document.getElementById("willingnessLabel1").style.color = "#4F4F4F";
  }
  else if (20 <= trust && trust < 40) {
    document.getElementById("willingnessLabel2").style.fontWeight = 'bold';
    document.getElementById("willingnessLabel2").style.color = "#4F4F4F";
  }
  else if (40 <= trust && trust < 60) {
    document.getElementById("willingnessLabel3").style.fontWeight = 'bold';
    document.getElementById("willingnessLabel3").style.color = "#4F4F4F";
  }
  else if (60 <= trust && trust < 80) {
    document.getElementById("willingnessLabel4").style.fontWeight = 'bold';
    document.getElementById("willingnessLabel4").style.color = "#4F4F4F";
  }
  else if (80 <= trust && trust <= 100) {
    document.getElementById("willingnessLabel5").style.fontWeight = 'bold';
    document.getElementById("willingnessLabel5").style.color = "#4F4F4F";
  }
  var left = 2 + 2.88 * trust;
  document.getElementById("willingnessAmount").style.marginLeft = left + "px";
}

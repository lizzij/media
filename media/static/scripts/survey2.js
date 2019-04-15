function show(shown) {
  // document.getElementById("weatherClearAllStarsButton").style.display='none';
  // document.getElementById("clearAllStarsButton").style.display='none';
  var pages = ['page1', 'page2', 'page3', 'page4', 'page5', 'page6'];
  var pageIndex;
  for (pageIndex = 0; pageIndex < pages.length; pageIndex++) {
    pageId = pages[pageIndex];
    if (shown == pageId) {
        document.getElementById(shown).style='display: flex;flex-direction: column;position: relative;';
    }
    else {
      document.getElementById(pageId).style.display='none';
    }
  }
  return 0;
}

function signUpFeeSlide() {
  var value=document.getElementById("signUpFeeSlider").value;
  var signUpFeeAmount = `${value}元`;
  document.getElementById("signUpFeeAmount").value=signUpFeeAmount;
}

function outing1Slide() {
  document.getElementById("outing1Amount").value=document.getElementById("outing1").value
  var value=document.getElementById("outing1Amount").value;
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
  var left = 10 + 2.97 * value;
  document.getElementById("outing1Amount").style.left = left + "px";
}

function outing2Slide() {
  document.getElementById("outing2Amount").value=document.getElementById("outing2").value
  var value=document.getElementById("outing2Amount").value;
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
  var left = 10 + 2.97 * value;
  document.getElementById("outing2Amount").style.left = left + "px";
}

function outing3Slide() {
  document.getElementById("outing3Amount").value=document.getElementById("outing3").value
  var value=document.getElementById("outing3Amount").value;
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
  var left = 10 + 2.97 * value;
  document.getElementById("outing3Amount").style.left = left + "px";
}

function outing4Slide() {
  document.getElementById("outing4Amount").value=document.getElementById("outing4").value
  var value=document.getElementById("outing4Amount").value;
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
  var left = 10 + 2.97 * value;
  document.getElementById("outing4Amount").style.left = left + "px";
}

function outing5Slide() {
  document.getElementById("outing5Amount").value=document.getElementById("outing5").value
  var value=document.getElementById("outing5Amount").value;
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
  var left = 10 + 2.97 * value;
  document.getElementById("outing5Amount").style.left = left + "px";
}

function domesticWebsiteSlide() {
  var value=document.getElementById("domesticWebsiteSlider").value;
  var hours;
  var minutes;
  if (value > 180) {
    document.getElementById("domesticWebsiteAmount").value=`大于3小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("domesticWebsiteAmount").value=time;
  }
}

function foreignWebsiteSlide() {
  var value=document.getElementById("foreignWebsiteSlider").value;
  var hours;
  var minutes;
  if (value > 180) {
    document.getElementById("foreignWebsiteAmount").value=`大于3小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("foreignWebsiteAmount").value=time;
  }
}

function domesticMediaSlide() {
  var value=document.getElementById("domesticMediaSlider").value;
  var hours;
  var minutes;
  if (value > 180) {
    document.getElementById("domesticMediaAmount").value=`大于3小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("domesticMediaAmount").value=time;
  }
}

function foreignMediaSlide() {
  var value=document.getElementById("foreignMediaSlider").value;
  var hours;
  var minutes;
  if (value > 180) {
    document.getElementById("foreignMediaAmount").value=`大于3小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("foreignMediaAmount").value=time;
  }
}

function chatWithFriendsSlide() {
  var value=document.getElementById("chatWithFriendsSlider").value;
  var hours;
  var minutes;
  if (value > 180) {
    document.getElementById("chatWithFriendsAmount").value=`大于3小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("chatWithFriendsAmount").value=time;
  }
}

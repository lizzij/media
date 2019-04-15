function show(shown) {
  var pages = ['page1', 'page2', 'page3'];
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

function exerciseTimeSlide() {
  var value=document.getElementById("exerciseTimeSlider").value;
  var hours;
  var minutes;
  if (value >= 1200) {
    document.getElementById("exerciseTimeAmount").value=`大于或等于20小时`;
  }
  else {
    hours = Math.floor(value / 60);
    minutes = value % 60;
    var time = `${hours}小时 ${minutes}分钟`;
    document.getElementById("exerciseTimeAmount").value=time;
  }
}

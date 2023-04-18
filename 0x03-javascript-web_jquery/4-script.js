$('#toggle_header').click(function () {
  $('header').addClass(function (index, currentClass) {
    if (currentClass === 'red') {
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }
  });
});

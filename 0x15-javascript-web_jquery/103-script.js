$(function() {
  function translate() {
    let lang = $('#language_code').val();
    let url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keypress(function(e) {
    if (e.which == 13) {
      translate();
    }
  });
});

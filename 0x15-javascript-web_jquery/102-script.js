$(function() {
  $('#btn_translate').click(function() {
    let lang = $('#language_code').val();
    let url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  });
});

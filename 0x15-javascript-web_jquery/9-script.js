$.ajax(
  {
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (res) {
      $('#hello').text(res.hello);
    }
  }
);

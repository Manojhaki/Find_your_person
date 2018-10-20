// find the cooridinate
function geoFindMe() {
  var output = document.getElementById("out");
var name="nabin";
  function success(position) {
    var latitude  = position.coords.latitude;
    var longitude = position.coords.longitude;

    output.innerHTML = '<p>Latitude is ' + latitude + '<br>Longitude is ' + longitude + '</p>';
  }

  function error() {
    output.innerHTML = "Unable to retrieve your location";
  }

  output.innerHTML = "<p>Locating...</p>";

  navigator.geolocation.getCurrentPosition(success, error);
  <iframe src="https://maps.google.com/maps?q='+latitude+','+longitude+'&hl=en&z=14&amp;output=embed" width="100%" height="400" frameborder="0" style="border:0" allowfullscreen></iframe>
}

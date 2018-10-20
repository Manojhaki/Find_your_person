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

}

const RapidAPI = require('rapidapi-connect');

const rapid = new RapidAPI("Find_your_person", "ProjectKey");

rapid.call('PackageName', 'FunctionName', {
	'ParameterKey1': 'ParameterValue1',
	'ParameterKey2': 'ParameterValue2'
}).on('success', (payload)=>{
	 /*YOUR CODE GOES HERE*/
}).on('error', (payload)=>{
	 /*YOUR CODE GOES HERE*/
});

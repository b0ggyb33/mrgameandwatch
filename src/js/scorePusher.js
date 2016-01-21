

var xhrRequest = function (url, type, score, callback) 
{
  var xhr = new XMLHttpRequest();
  var json = JSON.stringify(
    {
      username: Pebble.getWatchToken(),
      score : score
    }
  );
  
  xhr.addEventListener("error", function(evt)
                       {
                         console.log("something went wrong");
                       });
  
  xhr.onload = function () 
  {
    callback(this.responseText);
  };
  xhr.open(type, url,true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(json);
};

var xhrRequestForUsername = function (url, type, callback) 
{
  var xhr = new XMLHttpRequest();
  
  var json = JSON.stringify(
    {
      username: Pebble.getWatchToken()
    }
  );
  
  xhr.addEventListener("error", function(evt)
                       {
                         console.log("something went wrong");
                       });
  
  xhr.onload = function () 
  {
    callback(this.responseText);
  };
  xhr.open(type, url,true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(json);
};

function sendScore(score) 
{
  var scoreToPush = score[0];
  console.log("score: ");
  console.log(scoreToPush);
  
  // Construct URL
  var url = "http://86.12.100.145:5000/json";
  
  // Push request to url
  xhrRequest(url, 'POST', scoreToPush,
    function(responseText) 
    {
      console.log("Response from server:");
      console.log(responseText);
    }      
  );
}
function getUserName()
{
  var url = "http://86.12.100.145:5000/json"; 
  // Push request to url
  xhrRequestForUsername(url, 'GET',
    function(responseText) 
    {
      console.log("Response from server:");
      console.log(responseText);
      var dict = {
      'KEY_FRIENDLY':responseText
      };
      
      // Send a string to Pebble
      Pebble.sendAppMessage(dict, function(e) 
      {
        console.log('Send name to c successful.');
      }, function(e) 
      {
        console.log('Send name to c failed!');
      });  
      
      
    }      
  );
}


// Listen for when the watchface is opened
Pebble.addEventListener('ready', 
  function(e) {
    console.log("PebbleKit JS ready!");
    console.log("Getting user name");
    getUserName();
  }
);

// Listen for when an AppMessage is received
Pebble.addEventListener('appmessage',
  function(e) {
    console.log("AppMessage received! Score ready to submit");
    sendScore(e.payload);
  }                     
);

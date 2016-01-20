

var xhrRequest = function (url, type, score, callback) 
{
  var xhr = new XMLHttpRequest();
  
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
  xhr.send(JSON.stringify(
    {
      "username": Pebble.getWatchToken(),
      "time": "2015-05-25T08:42:00Z",
      "score" : score
    }
  ))
};

function sendScore(score) 
{
  console.log(Pebble.getWatchToken())
  var scoreToPush = score[0];
  console.log(scoreToPush);
  
  // Construct URL
  var url = "http://b0ggyb33.co.uk:5000/json";//"http://b0ggyb33.co.uk/hello.json"; 
  
  // Push request to url
  xhrRequest(url, 'POST', scoreToPush,
    function(responseText) 
    {
      console.log("Response:");
      console.log(responseText);
    }      
  );
}

// Listen for when the watchface is opened
Pebble.addEventListener('ready', 
  function(e) {
    console.log("PebbleKit JS ready!");
    
  }
);

// Listen for when an AppMessage is received
Pebble.addEventListener('appmessage',
  function(e) {
    console.log("AppMessage received!");
    sendScore(e.payload);
  }                     
);

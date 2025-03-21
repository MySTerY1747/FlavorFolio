// INFO: This is a placeholder. The goal is to have 5 more recipes loaded dynamically when the user clicks the "Load More" button using AJAX.
$(document).ready(function () {
  $("#load-more").click(function () {
    $("<p>New dynamically added paragraph!</p>").appendTo("body");
  });
});

// Reusable function to send AJAX requests
function loadDoc(url, callback) {
  var xhttp = new XMLHttpRequest();

  // Define what happens when the response is ready
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) { // Request completed successfully
      callback(this); // Call the provided callback function with the response
    }
  };

  xhttp.open("GET", url, true); // Initialize the request
  xhttp.send(); // Send the request
}

// Example callback function to process the response
function processResponse(xhttp) {
  document.getElementById("demo1").innerHTML = xhttp.responseText;
}

// Usage: Send a request and specify the callback
loadDoc("https://example.com/data", processResponse);

$(document).ready(function () {
  $("#load-more").click(function () {
    var url = $(this).data("ajax-target");

    $(this).text("Loading...");

    $.ajax({
      url: url,
      type: "GET",
      success: function (data) {
        $("#load-more").before(data);

        var currentNum = parseInt($("#load-more").data("ajax-target").match(/\d+$/)[0]);
        var newNum = currentNum + 5;
        $("#load-more").data("ajax-target", $("#load-more").data("ajax-target").replace(/\d+$/, newNum));

        $("#load-more").text("Load More");

        // If no new recipes were loaded, hide the button
        if (data.trim() === "") {
          $("#load-more").hide();
        }
      },
      error: function () {
        $("#load-more").text("Error loading more recipes. Try again.");
      }
    });
  });
});

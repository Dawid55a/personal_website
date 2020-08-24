$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
});
$(document).ready(function () {
  $(".has-dropdown").click(function(){

    $(".has-dropdown").toggleClass("is-active");
  });
});

// Hamburger Js
function hamburger() {
  $("#menu-btn").click(function () {
    // Toggle Mobile Menu
    $("#menu-btn").toggleClass("open");
    // $('#menu').toggleClass('flex');
    $("#menu").toggleClass("hidden");
  });
}

// Toggle Filter
function toggleFilter() {
    $(".toggle-filter").click(function () {
        $(this).toggleClass("bg-zinc-200 shadow-lg translate-y-0.5");
    });
}

$(document).ready(function () {
  hamburger();
  toggleFilter();
});


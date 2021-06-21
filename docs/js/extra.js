if (document.location.hostname === "docs.opensafely.org") {
  var script = document.createElement("script");
  script.defer = true;
  script.setAttribute("data-domain", "docs.opensafely.org");
  script.setAttribute("data-api", "/pa/api/event");
  script.src = "/pa/js/script.js";
  document.head.appendChild(script);

  // Serve legacy compat script to IE11 users
  var ua = window.navigator.userAgent;
  var trident = ua.indexOf("Trident/");
  var msie = ua.indexOf("MSIE ");
  if (trident > 0 || msie > 0) {
    var script = document.createElement("script");
    script.defer = true;
    script.id = "plausible";
    script.setAttribute("data-domain", "docs.opensafely.org");
    script.src = "https://plausible.io/js/plausible.compat.js";
    document.head.appendChild(script);
  }
}

if (document.location.hostname === "docs.opensafely.org") {
  var ua = window.navigator.userAgent;
  var trident = ua.indexOf("Trident/");
  var msie = ua.indexOf("MSIE ");

  var script = document.createElement("script");
  script.defer = true;

  // Serve legacy compat script to IE users
  if (trident > 0 || msie > 0) {
    script.id = "plausible";
    script.setAttribute("data-domain", "docs.opensafely.org");
    script.src = "https://plausible.io/js/plausible.compat.js";
  } else {
    script.setAttribute("data-domain", "docs.opensafely.org");
    script.setAttribute("data-api", "/pa/api/event");
    script.src = "/pa/js/script.js";
  }

  document.head.appendChild(script);
}

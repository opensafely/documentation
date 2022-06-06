var domain = "docs.opensafely.org";

if (document.location.hostname === domain) {
  var script = document.createElement("script");
  script.defer = true;
  script.setAttribute("data-domain", domain);
  script.id = "plausible";
  script.src = "https://plausible.io/js/plausible.compat.js";

  document.head.appendChild(script);
}

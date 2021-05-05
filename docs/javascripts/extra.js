if (document.location.hostname === "docs.opensafely.org") {
  var script = document.createElement("script");
  script.async = true;
  script.defer = true;
  script.setAttribute("data-domain", "docs.opensafely.org");
  script.src = "https://pa.opensafely.org/js/index.js";
  document.head.appendChild(script);
}

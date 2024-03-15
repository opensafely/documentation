const domain = "docs.opensafely.org";

if (document.location.hostname === domain) {
  const script = document.createElement("script");
  script.defer = true;
  script.setAttribute("data-domain", domain);
  script.id = "plausible";
  script.src = "https://plausible.io/js/plausible.compat.js";

  document.head.appendChild(script);
}

document.addEventListener("DOMContentLoaded", () => {
  patchCopyCodeButtons();
});

function patchCopyCodeButtons() {
  // select all "copy" buttons whose target selector is a <code> element
  codeCopyButtons = document.querySelectorAll(
    'button.md-clipboard[data-clipboard-target$="code"]',
  );
  for (const btn of codeCopyButtons) {
    const codeTextToCopy = getTextWithoutPromptAndOutput(
      btn.dataset.clipboardTarget,
    );
    btn.dataset.clipboardText = codeTextToCopy;
  }
}

function getTextWithoutPromptAndOutput(targetSelector) {
  const targetElement = document.querySelector(targetSelector);

  // exclude "Generic Prompt" and "Generic Output" spans from copy
  const excludedClasses = ["gp", "go"];

  let text = "";
  for (const node of targetElement.childNodes) {
    if (
      (node.nodeType == Node.TEXT_NODE) |
      (node.nodeType == Node.ELEMENT_NODE &&
        !excludedClasses.includes(node.className))
    ) {
      text += node.textContent;
    }
  }
  return text;
}

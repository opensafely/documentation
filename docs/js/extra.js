function getTextWithoutPromptAndOutput(targetSelector) {
  const targetElement = document.querySelector(targetSelector);

  // exclude "Generic Prompt" and "Generic Output" spans from copy
  const excludedClasses = ["gp", "go"];

  const clipboardText = [];
  [...targetElement.childNodes].map((node) => {
    // If the element does not contain the matching class,
    // add to the clipboard text array
    if (
      !excludedClasses.some((className) => node?.classList?.contains(className))
    ) {
      return clipboardText.push(node.textContent);
    }

    return null;
  });

  return clipboardText.join("").trim();
}

function patchCopyCodeButtons() {
  // select all "copy" buttons whose target selector is a <code> element
  [
    ...document.querySelectorAll(
      `button.md-clipboard[data-clipboard-target$="code"]`,
    ),
  ].map((btn) =>
    btn.setAttribute(
      "data-clipboard-text",
      getTextWithoutPromptAndOutput(btn.dataset.clipboardTarget),
    ),
  );
}

document.addEventListener("DOMContentLoaded", () => {
  patchCopyCodeButtons();
});

/**
 * Move the existing footer buttons to the main content section
 * @returns {void}
 */
function moveNavButtons() {
  /** @type {HTMLDivElement} */
  const contentArea = document.querySelector(`[data-md-component="content"]`);
  /** @type {HTMLElement} */
  const footerNav = document.querySelector(`[aria-label="Footer"]`);
  /** @type {HTMLElement} */
  const footClone = footerNav.cloneNode(true);
  footClone.classList.add("footer-nav-buttons");
  contentArea.appendChild(footClone);
  footerNav.setAttribute("hidden", "true");
}

/** @type {string[]} */
const buttonPaths = ["/getting-started/tutorial/", "/ehrql/tutorial/"];
/** @type {string} */
const docPath = window.location.pathname;

for (const path of buttonPaths) {
  if (docPath.startsWith(path)) {
    moveNavButtons();
  }
}

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
 * Move the existing footer buttons to the main content section to make them more visible.
 * Material MKDocs doesn’t seem to have any options to do this natively.
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
const buttonPaths = [
  "/ehrql/tutorial/",
  "/getting-started/tutorial/",
  "/outputs/output-checking/",
  "/outputs/releasing-overview/",
  "/outputs/requesting-file-release/",
  "/outputs/sdc/",
  "/outputs/viewing-released-files/",
];
/** @type {string} */
const docPath = window.location.pathname;

for (const path of buttonPaths) {
  if (docPath.startsWith(path)) {
    moveNavButtons();
  }
}

// Create a details component
function feedbackForm() {
  const el = document.createElement("details-utils");
  el.setAttribute("close-click-outside", "");
  el.setAttribute("close-esc", "");
  el.innerHTML = `
    <details class="feedback-form" id="feedbackForm">
      <summary class="feedback-form__summary">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" height="24" width="24" class="feedback-form__icon">
          <path stroke-linecap="round" stroke-linejoin="round" d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
        </svg>
        Give us feedback
      </summary>
      <div class="feedback-form__content">
        <p>Your feedback helps the OpenSAFELY team improve your experience.</p>
        <a
          class="feedback-form__button"
          href="#"
          target="_blank"
          rel="noopener noreferrer"
        >
          Provide feedback &nearr;&#xFE0E;
        </a>
        <p>
          For anything else,
          <a href="/how-to-get-help/">find out how to get help</a>.
        </p>
      </div>
    </details>
  `
  document.body.appendChild(el);
}

// Attach it to the page
feedbackForm();
// And then import details-utils
import "./details-utils.mjs";

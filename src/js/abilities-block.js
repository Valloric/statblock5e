import {createCustomElement} from './helpers/create-custom-element.js';
import './tapered-rule.js';

// Inline extraction START
function abilityModifier(abilityScore) {
  let score = parseInt(abilityScore, 10);
  return Math.floor((score - 10) / 2);
}

function formattedModifier(abilityModifier) {
  if (abilityModifier >= 0) {
    return '+' + abilityModifier;
  }
  // This is an en dash, NOT a "normal" dash. The minus sign needs to be more
  // visible.
  return '–' + Math.abs(abilityModifier);
}

function abilityText(abilityScore) {
  return [String(abilityScore),
          ' (',
          formattedModifier(abilityModifier(abilityScore)),
          ')'].join('');
}

function elementClass(contentNode) {
  return class extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({mode: 'open'})
        .appendChild(contentNode.cloneNode(true));
    }
    connectedCallback() {
      let root = this.shadowRoot;
      for (let i = 0; i < this.attributes.length; i++) {
        let attribute = this.attributes[i];
        let abilityShortName = attribute.name.split('-')[1];
        root.getElementById(abilityShortName).textContent =
           abilityText(attribute.value);
      }
    }
  }
}
// Inline extraction END

fetch('src/templates/abilities-block.html')
  .then(stream => stream.text())
  .then(htmlContent => {
    let contentNode =
      document.createRange().createContextualFragment(htmlContent);
    createCustomElement('abilities-block', contentNode, elementClass);
  });

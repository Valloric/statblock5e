import {createCustomElement} from './helpers/create-custom-element.js';

fetch('./src/templates/creature-heading.html')
  .then(stream => stream.text())
  .then(htmlContent => {
    let contentNode =
      document.createRange().createContextualFragment(htmlContent);
    createCustomElement('creature-heading', contentNode);
  });

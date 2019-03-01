import {createCustomElement} from './helpers/create-custom-element.js';

fetch('./src/templates/property-block.html')
  .then(stream => stream.text())
  .then(htmlContent => {
    let contentNode =
      document.createRange().createContextualFragment(htmlContent);
    createCustomElement('property-block', contentNode);
  });

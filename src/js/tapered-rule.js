import {createCustomElement} from '/src/js/helpers/create-custom-element.js';

fetch('src/templates/tapered-rule.html')
  .then(stream => stream.text())
  .then(htmlContent => {
    let contentNode =
      document.createRange().createContextualFragment(htmlContent);
    createCustomElement('tapered-rule', contentNode);
  });

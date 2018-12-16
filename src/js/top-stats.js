import {createCustomElement} from '/src/js/helpers/create-custom-element.js';
import '/src/js/tapered-rule.js';

fetch('src/templates/top-stats.html')
  .then(stream => stream.text())
  .then(htmlContent => {
    let contentNode =
      document.createRange().createContextualFragment(htmlContent);
    createCustomElement('top-stats', contentNode);
  });

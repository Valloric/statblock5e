export function createCustomElement(name, contentNode, elementClass = null) {
  if(elementClass === null) {
    customElements.define(name,
      class extends HTMLElement {
        constructor() {
          super();
          this.attachShadow({mode: 'open'})
            .appendChild(contentNode.cloneNode(true));
        }
      }
    )
  } else {
    customElements.define(name, elementClass(contentNode));
  }
}

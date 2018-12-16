<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>Statblock example</title><link href="//fonts.googleapis.com/css?family=Noto+Sans:400,700,400italic,700italic" rel="stylesheet" type="text/css"/><link href="//fonts.googleapis.com/css?family=Libre+Baskerville:700" rel="stylesheet" type="text/css"/><style>
    body {
      margin: 0;
    }

    stat-block {
      /* A bit of margin for presentation purposes, to show off the drop
      shadow. */
      margin-left: 20px;
      margin-top: 20px;
    }
  </style><script>function createCustomElement(name, contentNode, elementClass = null) {
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
</script></head><body><template id="stat-block"><style>
  .bar {
    height: 5px;
    background: #E69A28;
    border: 1px solid #000;
    position: relative;
    z-index: 1;
  }

  :host {
    display: inline-block;
  }

  #content-wrap {
    font-family: 'Noto Sans', 'Myriad Pro', Calibri, Helvetica, Arial,
                  sans-serif;
    font-size: 13.5px;
    background: #FDF1DC;
    padding: 0.6em;
    padding-bottom: 0.5em;
    border: 1px #DDD solid;
    box-shadow: 0 0 1.5em #867453;

    /* We don't want the box-shadow in front of the bar divs. */
    position: relative;
    z-index: 0;

    /* Leaving room for the two bars to protrude outwards */
    margin-left: 2px;
    margin-right: 2px;

    /* This is possibly overriden by next CSS rule. */
    width: 400px;

    -webkit-columns: 400px;
       -moz-columns: 400px;
            columns: 400px;
    -webkit-column-gap: 40px;
       -moz-column-gap: 40px;
            column-gap: 40px;

    /* We can't use CSS3 attr() here because no browser currently supports it,
       but we can use a CSS custom property instead. */
    height: var(--data-content-height);

    /* When height is constrained, we want sequential filling of columns. */
    -webkit-column-fill: auto;
       -moz-column-fill: auto;
            column-fill: auto;
  }

  :host([data-two-column]) #content-wrap {
    /* One column is 400px and the gap between them is 40px. */
    width: 840px;
  }

  ::slotted(h3) {
    border-bottom: 1px solid #7A200D;
    color: #7A200D;
    font-size: 21px;
    font-variant: small-caps;
    font-weight: normal;
    letter-spacing: 1px;
    margin: 0;
    margin-bottom: 0.3em;

    break-inside: avoid-column;
    break-after: avoid-column;
  }

  /* For user-level p elems. */
  ::slotted(p) {
    margin-top: 0.3em;
    margin-bottom: 0.9em;
    line-height: 1.5;
  }

  /* Last child shouldn't have bottom margin, too much white space. */
  ::slotted(*:last-child) {
    margin-bottom: 0;
  }
</style><div class="bar"></div><div id="content-wrap">
  <slot></slot>
</div><div class="bar"></div></template><script>{
  let templateElement = document.getElementById('stat-block');
  createCustomElement('stat-block', templateElement.content);
}</script><template id="creature-heading"><style>
  ::slotted(h1) {
    font-family: 'Libre Baskerville', 'Lora', 'Calisto MT',
                 'Bookman Old Style', Bookman, 'Goudy Old Style',
                 Garamond, 'Hoefler Text', 'Bitstream Charter',
                 Georgia, serif;
    color: #7A200D;
    font-weight: 700;
    margin: 0px;
    font-size: 23px;
    letter-spacing: 1px;
    font-variant: small-caps;
  }

  ::slotted(h2) {
    font-weight: normal;
    font-style: italic;
    font-size: 12px;
    margin: 0;
  }
</style><slot></slot></template><script>{
  let templateElement = document.getElementById('creature-heading');
  createCustomElement('creature-heading', templateElement.content);
}</script><template id="tapered-rule"><style>
  svg {
    fill: #922610;
    /* Stroke is necessary for good antialiasing in Chrome. */
    stroke: #922610;
    margin-top: 0.6em;
    margin-bottom: 0.35em;
  }
</style><svg height="5" width="400">
  <polyline points="0,0 400,2.5 0,5"></polyline>
</svg></template><script>{
  let templateElement = document.getElementById('tapered-rule');
  createCustomElement('tapered-rule', templateElement.content);
}</script><template id="top-stats"><style>
  ::slotted(*) {
    color: #7A200D;
  }
</style><tapered-rule></tapered-rule><slot></slot><tapered-rule></tapered-rule></template><script>{
  let templateElement = document.getElementById('top-stats');
  createCustomElement('top-stats', templateElement.content);
}</script><template id="abilities-block"><style>
  table {
    width: 100%;
    border: 0px;
    border-collapse: collapse;
  }
  th, td {
    width: 50px;
    text-align: center;
  }
</style><tapered-rule></tapered-rule><table>
  <tbody><tr>
    <th>STR</th>
    <th>DEX</th>
    <th>CON</th>
    <th>INT</th>
    <th>WIS</th>
    <th>CHA</th>
  </tr>
  <tr>
    <td id="str"></td>
    <td id="dex"></td>
    <td id="con"></td>
    <td id="int"></td>
    <td id="wis"></td>
    <td id="cha"></td>
  </tr>
</tbody></table><tapered-rule></tapered-rule></template><script>{
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

  let templateElement = document.getElementById('abilities-block');
  createCustomElement('abilities-block', templateElement.content, elementClass);
}</script><template id="property-line"><style>
  :host {
    line-height: 1.4;
    display: block;
    text-indent: -1em;
    padding-left: 1em;
  }

  ::slotted(h4) {
    margin: 0;
    display: inline;
    font-weight: bold;
  }

  ::slotted(p:first-of-type) {
    display: inline;
    text-indent: 0;
  }

  ::slotted(p) {
    text-indent: 1em;
    margin: 0;
  }
</style><slot></slot></template><script>{
  let templateElement = document.getElementById('property-line');
  createCustomElement('property-line', templateElement.content);
}</script><template id="property-block"><style>
  :host {
    margin-top: 0.3em;
    margin-bottom: 0.9em;
    line-height: 1.5;
    display: block;
  }

  ::slotted(h4) {
    margin: 0;
    display: inline;
    font-weight: bold;
    font-style: italic;
  }

  ::slotted(p:first-of-type) {
    display: inline;
    text-indent: 0;
  }

  ::slotted(p) {
    text-indent: 1em;
    margin: 0;
  }
</style><slot></slot></template><script>{
  let templateElement = document.getElementById('property-block');
  createCustomElement('property-block', templateElement.content);
}</script><stat-block>
    <creature-heading>
      <h1>Animated Armor</h1>
      <h2>Medium construct, unaligned</h2>
    </creature-heading>

    <top-stats>
      <property-line>
        <h4>Armor Class</h4>
        <p>18 (natural armor)</p>
      </property-line>
      <property-line>
        <h4>Hit Points</h4>
        <p>33 (6d8 + 6)</p>
      </property-line>
      <property-line>
        <h4>Speed</h4>
        <p>25ft</p>
      </property-line>

      <abilities-block data-cha="1" data-con="13" data-dex="11" data-int="1" data-str="14" data-wis="3"></abilities-block>

      <property-line>
        <h4>Damage Immunities</h4>
        <p>poison, psychic</p>
      </property-line>
      <property-line>
        <h4>Condition Immunities</h4>
        <p>blinded, charmed, deafened, exhaustion, frightened, paralyzed,
          petrified, poisoned</p>
      </property-line>
      <property-line>
        <h4>Senses</h4>
        <p>blindsight 60 ft. (blind beyond this radius), passive Perception 6</p>
      </property-line>
      <property-line>
        <h4>Languages</h4>
        <p>—</p>
      </property-line>
      <property-line>
        <h4>Challenge</h4>
        <p>1 (200 XP)</p>
      </property-line>
    </top-stats>

    <property-block>
      <h4>Antimagic Susceptibility.</h4>
      <p>The armor is incapacitated while in the area of an <i>antimagic
        field</i>.  If targeted by <i>dispel magic</i>, the armor must succeed
        on a Constitution saving throw against the caster’s spell save DC or
        fall unconscious for 1 minute.</p>
    </property-block>
    <property-block>
      <h4>False Appearance.</h4>
      <p>While the armor remains motionless, it is indistinguishable from a
        normal suit of armor.</p>
    </property-block>

    <h3>Actions</h3>

    <property-block>
      <h4>Multiattack.</h4>
      <p>The armor makes two melee attacks.</p>
    </property-block>

    <property-block>
      <h4>Slam.</h4>
      <p><i>Melee Weapon Attack:</i> +4 to hit, reach 5 ft., one target.
        <i>Hit:</i> 5 (1d6 + 2) bludgeoning damage.</p>
    </property-block>
  </stat-block></body></html>

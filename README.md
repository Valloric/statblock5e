# &lt;hello-world&gt;

> A Web Component example using [VanillaJS](http://vanilla-js.com/).
>
> Looking for a boilerplate? Check [element-boilerplate](https://github.com/webcomponents/element-boilerplate).

## Demo

[Check it live!](http://webcomponents.github.io/hello-world-element)

## Install

Install the component using [Bower](http://bower.io/):

```sh
$ bower install hello-world-element --save
```

Or [download as ZIP](https://github.com/webcomponents/hello-world-element/archive/master.zip).

## Usage

1. Import Web Components' polyfill:

    ```html
    <script src="bower_components/platform/platform.js"></script>
    ```

2. Import Custom Element:

    ```html
    <link rel="import" href="bower_components/hello-world-element/dist/hello-world.html">
    ```

3. Start using it!

    ```html
    <hello-world></hello-world>
    ```

## Options

Attribute  | Options                   | Default             | Description
---        | ---                       | ---                 | ---
`who`      | *string*                  | `World`             | Who do you want to say hello?

## Development

In order to run it locally you'll need to fetch some dependencies and a basic server setup.

1. Install [Bower](http://bower.io/) & [Grunt](http://gruntjs.com/):

    ```sh
    $ [sudo] npm install -g bower grunt-cli
    ```

2. Install local dependencies:

    ```sh
    $ bower install && npm install
    ```

3. To test your project, start the development server and open `http://localhost:8000`.

    ```sh
    $ grunt server
    ```

4. To provide a live demo, send everything to `gh-pages` branch.

    ```sh
    $ grunt deploy
    ```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

For detailed changelog, check [Releases](https://github.com/webcomponents/hello-world-element/releases).

## License

[MIT License](http://webcomponentsorg.mit-license.org/) © WebComponents.org

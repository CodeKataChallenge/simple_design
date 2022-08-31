(function(document, Elm) {
    const container = document.getElementById('container');
    const app = Elm.Presentations.init({
        node: container,
    });

    window.app = app;
})(document, Elm);

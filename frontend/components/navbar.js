class Navbar extends HTMLElement {
    constructor() {
        super();

        this.innerHTML = /*html*/`
        <nav class="green darken-4">
            <div class="nav-wrapper container">
                <a href="#" class="brand-logo">MyPinterest</a>
                <ul class="right">
                    <li id="li-general"><a id="btn-general">Galería general</a></li>
                    <li id="li-misfotos"><a id="btn-misfotos">Mi galería</a></li>
                    <li id="li-uploader"><a id="btn-uploader">Subir foto</a></li>
                    <li id="li-logout">
                        <a class="red-text text-lighten-5" id="btn-logout">Cerrar Sesión</a>
                    </li>
                </ul>
            </div>
        </nav>
        `
    }
}

customElements.define('my-navbar', Navbar);
// Extends es para heredar de super clases
class LoginLoader extends HTMLElement {
    constructor() {
        super();
        // this es como el self de python
        this.innerHTML = /*html*/`
            <div id="login-loader" class="center-align" style="margin-top: 20px;">
                <div class="preloader-wrapper big active">
                    <div class="spinner-layer spinner-green-darker">
                        <div class="circle-clipper left">
                            <div class="circle"></div>
                        </div>
                        <div class="gap-patch">
                            <div class="circle"></div>
                        </div>
                        <div class="circle-clipper right">
                            <div class="circle"></div>
                        </div>
                    </div>
                </div>
                <p>Iniciando sesión</p>
            </div>
        `;
    }
}

customElements.define('login-loader', LoginLoader);
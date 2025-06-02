class LoginForm extends HTMLElement {
    constructor() {
        super();
        this.innerHTML = /*html*/`
    <div class="login-container">
            <div class="row center-row">
                    <div class="card white z-depth-3">
                        <h5 class="login-title">Login</h5>
                            <div class="card-content">
                                <div class="input-field col s12">
                                    <i class="material-icons suffix">person</i>
                                    <input type="text" name="username" id="username" autocomplete="off" autofocus >
                                    <label class ="teal-text darken-1" for="username">Usuario</label>
                                </div>
                                <div class="input-field col s12">
                                    <i class="material-icons suffix">lock</i>
                                    <input type="password" name="password" id="password" autocomplete="off">
                                    <label class ="teal-text darken-1"  for="password">Contraseña</label>
                                </div>
                                    <button id="btnLogin" class="btn waves-effect waves-light">Entrar</button>
                            </div>
                    </div>
                </div>
            </div>
        </div>
        `;
    }
}

customElements.define('login-form', LoginForm);
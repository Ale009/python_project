class UserGreeting extends HTMLElement {
    constructor() {
        super();

        this.innerHTML = /*html*/`
            <!-- Muestra el nombre del usuario -->
            <h5 id="user-greeting" class="green-text text-darken-4"></h5>
        `
    }
}

customElements.define('user-greeting', UserGreeting);
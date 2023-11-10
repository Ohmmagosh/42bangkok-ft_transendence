import {
	ClassElement,
	LabelElement,
	InputElement,
	ButtonElement,
} from "./classElement.js";

function login() {

	const formElement = new ClassElement('form', 'container', 'loginForm', '');

	const divEmail = new ClassElement('div', 'form-group','','');
	const divPassword = new ClassElement('div', 'form-group', '', '');

	const labelEmail = new LabelElement('inputEmail', 'Email address');
	const inputEmail = new InputElement('email', 'form-control', 'inputEmail', 'Enter email');

	const labelPassword = new LabelElement('inputPassword', 'Password');
	const inputPassword = new InputElement('password', 'form-control', 'inputPassword', 'Password');

	const buttonLogin = new ButtonElement('button', 'btn btn-primary', 'buttonLogin', 'Login');

	divEmail.setAddElement(labelEmail.getElement());
	divEmail.setAddElement(inputEmail.getElement());

	divPassword.setAddElement(labelPassword.getElement());
	divPassword.setAddElement(inputPassword.getElement());



	formElement.setAddElement(divEmail.getElement());
	formElement.setAddElement(divPassword.getElement());
	formElement.setAddElement(buttonLogin.getElement());
	document.body.appendChild(formElement.getElement());
}

export default login;

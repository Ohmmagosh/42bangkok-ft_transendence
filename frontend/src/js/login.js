import {
	ClassElement,
	LabelElement,
	InputElement,
	ButtonElement,
} from "./classElement.js";

function login() {
	const divContainer = new ClassElement('div', 'd-flex justify-content-center align-items-center container-sm vh-100 vw-100 position-relative', 'loginContainer', '');
	const divRow = new ClassElement('div', 'row row-gap-3 justify-content-center align-items-center w-25 position-relative', 'loginRow', '');
	const	headerText = new ClassElement('h1', 'text-center ', 'loginHeader', 'Pong Game');
	const formElement = new ClassElement('form', 'row row-gap-3 ', 'loginForm', '');
	const divEmail = new ClassElement('div', 'form-group','','');
	const divPassword = new ClassElement('div', 'form-group', '', '');
	const labelEmail = new LabelElement('inputEmail', 'Email address');
	const inputEmail = new InputElement('email', 'form-control', 'inputEmail', 'Enter email');
	const labelPassword = new LabelElement('inputPassword', 'Password');
	const inputPassword = new InputElement('password', 'form-control', 'inputPassword', 'Password');
	const divButton = new ClassElement('div', 'form-group d-flex justify-content-end', '', '');
	const buttonLogin = new ButtonElement('button', 'btn btn-primary w-25 ', 'buttonLogin', 'Login');

	divEmail.setAddElement(labelEmail.getElement());
	divEmail.setAddElement(inputEmail.getElement());

	divButton.setAddElement(buttonLogin.getElement());

	divPassword.setAddElement(labelPassword.getElement());
	divPassword.setAddElement(inputPassword.getElement());

	formElement.setAddElement(divEmail.getElement());
	formElement.setAddElement(divPassword.getElement());
	formElement.setAddElement(divButton.getElement());

	divRow.setAddElement(headerText.getElement());
	divRow.setAddElement(formElement.getElement());
	divContainer.setAddElement(divRow.getElement());
	document.body.appendChild(divContainer.getElement());
}

export default login;

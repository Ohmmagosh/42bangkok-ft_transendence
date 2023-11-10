import {
	ClassElement,
	LabelElement,
	InputElement,
	ButtonElement,
} from "./classElement.js";

function login() {
	const divContainer = new ClassElement('div', 'd-flex justify-content-center align-items-center container-sm vh-100 vw-100 position-relative', 'loginContainer', '');
	const divRow = new ClassElement('div', 'row', 'loginRow', '');
	const	headerText = new ClassElement('h1', 'text-center', 'loginHeader', 'Login');
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

	// divContainer.setAddElement(formElement.getElement());
	divRow.setAddElement(headerText.getElement());
	divRow.setAddElement(formElement.getElement());
	divContainer.setAddElement(divRow.getElement());
	document.body.appendChild(divContainer.getElement());
	// document.body.appendChild(label.getElement());
}

export default login;

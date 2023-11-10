export class ClassElement {
	constructor( tag, className, id, innerHTML) {
		this.ele = document.createElement(tag);
		this.ele.className = className;
		this.ele.innerHTML = innerHTML;
		this.ele.id = id;
	}
	getElement() {
		return this.ele;
	}
	setSetElement(ele) {
		this.ele = ele;
	}
	setAddElement(ele) {
		this.ele.appendChild(ele);
	}
	setId(id) {
		this.ele.id = id;
	}
	setClassName(className) {
		this.ele.className = className;
	}
	setInnerHTML(innerHTML) {
		this.ele.innerHTML = innerHTML;
	}
}

export class LabelElement {
	constructor(ifor, text) {
		this.ele = document.createElement('label');
		this.ele.htmlFor = ifor;
		this.ele.innerHTML = text;
	}

	getElement() {
		return this.ele;
	}
	setHtmlFor(htmlFor) {
		this.ele.htmlFor = htmlFor;
	}
}

export class InputElement {
	constructor(type, className, id, placeholder) {
		this.ele = document.createElement('input');
		this.ele.type = type;
		this.ele.className = className;
		this.ele.id = id;
		this.ele.placeholder = placeholder;
	}
	getElement() {
		return this.ele;
	}
	setType(type) {
		this.ele.type = type;
	}
	setClassName(className) {
		this.ele.className = className;
	}
	setId(id) {
		this.ele.id = id;
	}
	setPlaceholder(placeholder) {
		this.ele.placeholder = placeholder;
	}
}

export class ButtonElement {
	constructor(type, className, id, text, onclick) {
		this.ele = document.createElement('button');
		this.ele.type = type;
		this.ele.className = className;
		this.ele.id = id;
		this.ele.innerHTML = text;
		this.ele.onclick = onclick;
	}
	getElement() {
		return this.ele;
	}
	setType(type) {
		this.ele.type = type;
	}
	setClassName(className) {
		this.ele.className = className;
	}
	setId(id) {
		this.ele.id = id;
	}
	setInnerHTML(innerHTML) {
		this.ele.innerHTML = innerHTML;
	}
	setOnclick(onclick) {
		this.ele.onclick = onclick;
	}
}

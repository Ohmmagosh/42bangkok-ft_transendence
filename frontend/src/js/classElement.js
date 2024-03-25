export class ClassElement {
	constructor( tag , className, id, innerHTML) {
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

export class LabelElement extends ClassElement {
	constructor(ifor, className, text) {
		super('label', className, '', text);
		this.ele.htmlFor = ifor;
	}

	setHtmlFor(htmlFor) {
		this.ele.htmlFor = htmlFor;
	}
}

export class InputElement extends ClassElement {
	constructor(type, className, id, placeholder) {
		super('input', className, id, '');
		this.ele.type = type;
		this.ele.placeholder = placeholder;
	}
	setType(type) {
		this.ele.type = type;
	}
	setPlaceholder(placeholder) {
		this.ele.placeholder = placeholder;
	}
}

export class ButtonElement extends ClassElement {
	constructor(type, className, id, innerHTML, onclick) {
		super('button', className, id, innerHTML);
		this.ele.type = type;
		this.ele.onclick = onclick;
	}
	setType(type) {
		this.ele.type = type;
	}
	setOnclick(onclick) {
		this.ele.onclick = onclick;
	}
}

class State {
	constructor(state) {
		this.state = state;
	}
	getState() {
		return this.state;
	}
	setState(state) {
		this.state = state;
	}
}

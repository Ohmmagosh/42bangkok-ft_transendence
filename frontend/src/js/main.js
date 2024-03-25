// Import our custom CSS
// import path from require('path');
import '../scss/styles.scss';
// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap';

// Import THREE
// import * as THREE from 'three';
import render from './renderer';
import login from './login';

function main() {
	// let status = true;
	const path = require('path');
	document.body.className = "vw-100 vh-100 bg-black"
	login();
	console.log(__dirname)
	const res = async () => {
		const res = await fetch('./src/main/index.html').then(res => res.text());
		console.log(res);
	}
	res()

	// const test = async () => {
	// 	const res = await fetch('./src/main/index.html').then(res => res.text());
	// 	console.log(res);
	// }
	// test()
	// if (!status)
		// render();
}

main();


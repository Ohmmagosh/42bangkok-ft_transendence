// Import THREE
import * as THREE from 'three';

function render() {
	const divAnimation = document.createElement('div');
	const scene = new THREE.Scene();
	const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
	const renderer = new THREE.WebGLRenderer();
	const geometry = new THREE.BoxGeometry( 1, 1, 1 );
	const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
	const cube = new THREE.Mesh( geometry, material );


	divAnimation.id = 'animation';
	renderer.setSize( window.innerWidth, window.innerHeight );
	divAnimation.appendChild(renderer.domElement);
	document.body.appendChild( divAnimation );
	scene.add( cube );

	camera.position.z = 5;

	const animate = () => {
		requestAnimationFrame(animate);
		cube.rotation.x += 0.01;
		cube.rotation.y += 0.01;
		renderer.render(scene, camera);
	}
	animate();
}

export default render;

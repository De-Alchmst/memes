// very little js
// just as it should be

let wasm = null;

// load wasm from fokin base64 because servers suck
// I just want to click my fockMothering .html file and do my fokin math
// for some reason the web does not support just loading files, so enjoy the look
// at my wasm base 64
function getWASM() {
	const wasmBased64 = "AGFzbQEAAAABEQNgAX4BfmABfQF9YAJ9fwF9AwcGAAABAQECBgkBfQBD2w9JQAsHSAUJZmFjdG9yaWFsAAAJZmlib25hY2NpAAENY2lyY3VtZmVyZW5jZQACDWNpcmNsZVN1cmZhY2UAAwxzcGhlcmVWb2x1bWUABAq4AQYxAQF+QgEhASAAQgFZBEAgACEBA0AgAEIBfSEAIABCAFIEQCABIAB+IQEMAQsLCyABCy0BAn5CACEBQgEhAgNAIABCAVUEQCABIAIhASACfCECIABCAX0hAAwBCwsgAQsNACMAIACUQwAAAECUCwoAIAAgAJQjAJQLFwBDAACAQEMAAEBAlSMAlCAAQQMQBZQLJQEBfUMAAIA/IQIDQCABBEAgAiAAlCECIAFBAWshAQwBCwsgAgs=";
	const wasmBinary = Uint8Array.from(atob(wasmBased64), c => c.charCodeAt(0));

	WebAssembly.instantiate(wasmBinary).then(result => wasm = result.instance.exports);
}

// all the forms
const fact = document.getElementById("factorial");
const factNum = document.getElementById("fact-number");
const factResult = document.getElementById("fact-result");

const fib = document.getElementById("fibonacci");
const fibNum = document.getElementById("fib-number");
const fibResult = document.getElementById("fib-result");

const circumference = document.getElementById("circumference");
const circumferenceNum = document.getElementById("circumference-number");
const circumferenceResult = document.getElementById("circumference-result");

// there's a lot of them
const circleSurface = document.getElementById("circleSurface");
const circleSurfaceNum = document.getElementById("circleSurface-number");
const circleSurfaceResult = document.getElementById("circleSurface-result");

const sphereVolume = document.getElementById("sphereVolume");
const sphereVolumeNum = document.getElementById("sphereVolume-number");
const sphereVolumeResult = document.getElementById("sphereVolume-result");

// calling the wasm
fact.addEventListener("submit", function(event){
   event.preventDefault();
   factResult.innerText = "result: " + String(wasm.factorial(BigInt(factNum.value)));
});

fib.addEventListener("submit", function(event){
   event.preventDefault();
   fibResult.innerText = "result: " + String(wasm.fibonacci(BigInt(fibNum.value)));
})

circumference.addEventListener("submit", function(event){
   event.preventDefault();
   circumferenceResult.innerText = "result: " + wasm.circumference(Number(circumferenceNum.value)).toFixed(4); // my number is too good
})

circleSurface.addEventListener("submit", function(event){
   event.preventDefault();
   circleSurfaceResult.innerText = "result: " + wasm.circleSurface(Number(circleSurfaceNum.value)).toFixed(4);
})

sphereVolume.addEventListener("submit", function(event){
   event.preventDefault();
   sphereVolumeResult.innerText = "result: " + wasm.sphereVolume(Number(sphereVolumeNum.value)).toFixed(4);
})

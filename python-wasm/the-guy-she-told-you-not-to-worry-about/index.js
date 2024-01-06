let wasm = null;

// load wasm from fokin base64 because servers suck
// I just want to click my fockMothering .html file and do my fokin math
// for some reason the web does not support just loading files, so enjoy the look
// at my wasm base 64
function getWASM() {
	const wasmBased64 = "AGFzbQEAAAABEQNgAX8Bf2ABfQF9YAJ9fwF9AwcGAAABAQECBgkBfQBD2w9JQAsHSAUJZmFjdG9yaWFsAAAJZmlib25hY2NpAAENY2lyY3VtZmVyZW5jZQACDWNpcmNsZVN1cmZhY2UAAwxzcGhlcmVWb2x1bWUABAq4AQYxAQF/QQEhASAAQQFOBEAgACEBA0AgAEEBayEAIABBAEcEQCABIABsIQEMAQsLCyABCy0BAn9BACEBQQEhAgNAIABBAUoEQCABIAIhASACaiECIABBAWshAAwBCwsgAQsNACMAIACUQwAAAECUCwoAIAAgAJQjAJQLFwBDAACAQEMAAEBAlSMAlCAAQQMQBZQLJQEBfUMAAIA/IQIDQCABBEAgAiAAlCECIAFBAWshAQwBCwsgAgs=";
	const wasmBinary = Uint8Array.from(atob(wasmBased64), c => c.charCodeAt(0));

	WebAssembly.instantiate(wasmBinary).then(result => wasm = result.instance.exports);
}

function test() {
   console.log(wasm.factorial(5))
   console.log(wasm.fibonacci(8))
   console.log(wasm.circumference(4.53))
   console.log(wasm.circleSurface(4.53))
   console.log(wasm.sphereVolume(4.53))
}

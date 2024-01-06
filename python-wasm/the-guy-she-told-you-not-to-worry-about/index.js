let wasm = null;

// load wasm from fokin base64 because servers suck
// I just want to click my fockMothering .html file and do my fokin math
// for some reason the web does not support just loading files, so enjoy the look
// at my wasm base 64
function getWASM() {
	const wasmBased64 = "AGFzbQEAAAABBgFgAX8BfwMDAgAABxkCCWZhY3RvcmlhbAAACWZpYm9uYWNjaQABCmECMQEBf0EBIQEgAEEBTgRAIAAhAQNAIABBAWshACAAQQBHBEAgASAAbCEBDAELCwsgAQstAQJ/QQAhAUEBIQIDQCAAQQFKBEAgASACIQEgAmohAiAAQQFrIQAMAQsLIAEL";
	const wasmBinary = Uint8Array.from(atob(wasmBased64), c => c.charCodeAt(0));

	WebAssembly.instantiate(wasmBinary).then(result => wasm = result.instance.exports);
}

function test() {
   console.log(wasm.factorial(5))
   console.log(wasm.fibonacci(8))
}

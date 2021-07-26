const triggers = {}
let port = null


function emit (event, data) {
  const message = { event, ...data }
  if (port) {
    port.postMessage(message)
  }
}

function on (event, fn) {
  if (triggers[event]) {
    triggers[event].push(fn)
  } else {
    triggers[event] = [ fn ]
  }
}

function receiveMessage (e) {
  if (e.ports && e.ports[0]) {
    port = e.ports[0]
    port.onmessage = receiveMessage
    document.body.className = 'embed'
  }

  const message = { ...e.data }
  const event = message.event
  delete message.event
  const fns = triggers[event]
  if (fns) {
    fns.forEach(fn => fn(message))
  }
}

window.addEventListener('message', receiveMessage)

export default { emit, on }

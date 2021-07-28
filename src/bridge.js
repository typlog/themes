const triggers = {}
let port = null


function emit (event, data = {}) {
  const message = { event, ...data }
  if (port) {
    port.postMessage(JSON.stringify(message))
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
  }

  try {
    const message = JSON.parse(e.data)
    const event = message.event
    delete message.event
    const fns = triggers[event]
    if (fns) {
      fns.forEach(fn => fn(message))
    }
  } catch (e) {}
}

window.addEventListener('message', receiveMessage)

export default { emit, on }

document.getElementById('formUrlShorten').addEventListener('submit', (event)=>{
    event.preventDefault()
    
    const urlOriginal = document.getElementById('urlOriginal').value
    const urlResult = document.getElementById('resultUrlShorten')

    console.log(urlOriginal)

    fetch('/short/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"url": urlOriginal})
    })
    .then(response => response.json()).then(data => {
        urlResult.value = data.short_url
    })
    .catch(error => {
        console.error('Error: ', error)
    })
})

document.getElementById('btnCopy').addEventListener('click', (event)=>{
    const urlResult = document.getElementById('resultUrlShorten')
    navigator.clipboard.writeText(urlResult.value)
})


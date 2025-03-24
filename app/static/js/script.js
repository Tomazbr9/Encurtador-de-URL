document.getElementById('formUrlShorten').addEventListener('submit', (event)=>{
    event.preventDefault()
    
    const urlOriginal = document.getElementById('urlOriginal').value
    const urlResult = document.getElementById('resultUrlShorten')
    const urlMessageError = document.getElementById('urlMessageError')
    urlResult.value = ''

    fetch('/short/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({"url": urlOriginal})
    })
    .then(response => {
        if(!response.ok){
            return response.json().then(data => {    
                urlMessageError.style.display = 'block'
                urlMessageError.textContent = data.message 
            })
        }
        return response.json()

    }).then(data => {
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


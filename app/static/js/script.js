const formUrlShorten = document.getElementById('formUrlShorten')
if(formUrlShorten){
    formUrlShorten.addEventListener('submit', async (event)=>{
        event.preventDefault()
        
        const urlOriginal = document.getElementById('urlOriginal').value
        const urlResult = document.getElementById('resultUrlShorten')
        const urlMessageError = document.getElementById('urlMessageError')
        urlResult.value = ''

        await fetch('/short/', {
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
            urlMessageError.style.display = 'block'
            urlMessageError.textContent = error.message
            console.error('Error: ', error)
        })
    })
}

const btnCopy = document.getElementById('btnCopy')
if(btnCopy){
    document.getElementById('btnCopy').addEventListener('click', (event)=>{
        const urlResult = document.getElementById('resultUrlShorten')
        navigator.clipboard.writeText(urlResult.value)
    })
}

const formLogin = document.getElementById('formLogin')
if(formLogin){
    formLogin.addEventListener('submit', async (event)=>{
        event.preventDefault()

        const usernameLogin = document.getElementById('usernameLogin').value
        const passwordLogin = document.getElementById('passwordlogin').value
        const loginMessageError = document.getElementById('loginMessageError')

        credentials = `${usernameLogin}:${passwordLogin}`

        try {
            const response = await fetch('/login_user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Basic ${btoa(credentials)}`
                }
            })

            const data = await response.json()

            if (response.ok) {
                loginMessageError.style.display = 'none'
                window.location.href = '/home'
            } else {
                loginMessageError.style.display = 'block'
                loginMessageError.textContent = data.detail || 'Usuário ou senha inválidos'
            }
        } catch (error) {
            loginMessageError.style.display = 'block'
            loginMessageError.textContent = error.message || 'Erro ao fazer login'
        }
    })
}

const formRegister = document.getElementById('formRegister')
if(formRegister){
    document.getElementById('formRegister').addEventListener('submit', async (event)=>{
        event.preventDefault()

        const usernameLogin = document.getElementById('usernameLogin').value
        const passwordLogin = document.getElementById('passwordlogin').value
        const loginMessageError = document.getElementById('loginMessageError')

        await fetch('/register_user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify(
                {'username': usernameLogin, 'password': passwordLogin}
            )
        }).then(response => response.json()).then(data => {
            loginMessageError.style.display = 'block'
            loginMessageError.textContent = data.message
        }).catch(error => {
            loginMessageError.style.display = 'block'
            loginMessageError.textContent = 'Erro ao fazer registro'
        })
    })
}

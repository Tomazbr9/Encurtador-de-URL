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

        try {
            const response = await fetch('/login_user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'username': usernameLogin, 'password': passwordLogin
                })
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

        const usernameRegister = document.getElementById('usernameLogin').value
        const passwordRegister = document.getElementById('passwordlogin').value
        const registerMessageError = document.getElementById('loginMessageError')

        try {
            const response = await fetch('/register_user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'username': usernameRegister, 'password': passwordRegister
                })
            })

            const data = await response.json()

            if (response.ok) {
                loginMessageError.style.display = 'none'
                window.location.href = '/login'
            } else {
                registerMessageError.style.display = 'block'
                registerMessageError.textContent = data.detail || 'Usuário ou senha inválidos'
            }
        } catch (error) {
            loginMessageError.style.display = 'block'
            loginMessageError.textContent = error.message || 'Erro ao fazer login'
        }
    })
}

const logout = document.getElementById('logout')
if(logout){
    logout.addEventListener('click', async ()=>{

        const response = await fetch('/logout')

        if(response){
            window.location.href = '/home'
        } 
        else {
            console.log("Erro ao fazer logout")
        }
    })
}

async function deleteUrl(id){

    const response = await fetch(`/delete_url/${id}/`, {
        method: 'DELETE'
    })
    
    const data = response.json()

    if(response){
        location.reload()
    }
    else {
        console.error('Erro ao deletar url')
    }
}
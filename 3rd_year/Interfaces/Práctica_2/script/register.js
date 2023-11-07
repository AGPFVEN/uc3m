const form = document.getElementById('form')
const formElements = form.querySelectorAll(".register--input-wrapper")
const formCheckBox = form.querySelector(".register--form-switch")
const formCheckBoxInput = formCheckBox.getElementsByTagName("input")
let formElement
let formElementInput
let formElementError
let successfulInput

form.addEventListener('submit', (e) => {
    successfulInput = true

    for (let i = 0; i < formElements.length; i++){
        formElement = formElements[i]
        formElementInput = formElement.querySelector(".register--input")
        formElementError = formElement.querySelector(".register--error")
        if (formElementInput.value === '' || formElementInput.value == null){
            formElementError.textContent = "Campo debe ser rellenado"
            successfulInput = false
            e.preventDefault()
        }
        else{
            formElementError.textContent = ''
            switch (formElement.id){
                case 'email': 
                    if (formElementInput.value.replace(/[^@]/g, "").length != 1){
                        formElementError.textContent = "Debe haber un @ en tu correo"
                        successfulInput = false
                        e.preventDefault()
                    } else {
                        let arroba = false
                        let validDot = false
                        for (let i = 0; i < formElementInput.value.length; i++){
                            if (formElementInput.value[i] == "@"){
                                arroba = true
                            }
                            if (formElementInput.value[i] == "." && arroba == true){
                                validDot = true
                            }
                        }
                        if (validDot != true){
                            formElementError.textContent = "Formato de correo no valido"
                            successfulInput = false
                            e.preventDefault()
                        }
                    }
                    //let arroba = false
                break
                case 'fullName': 
                    for (let i = 0; i < formElementInput.value.length; i++){
                        if ((formElementInput.value[i] >= '0' && formElementInput.value[i] <= '9')){    
                            formElementError.textContent = "No pueden haber números en tu nombre completo"
                            successfulInput = false
                            e.preventDefault()
                        } 
                    }
                break

                case 'phoneNumber':
                    if (formElementInput.value.length == 9){
                        for (let i = 0; i < formElementInput.value.length; i++){
                            if (!(formElementInput.value[i] >= '0' && formElementInput.value[i] <= '9')){    
                                formElementError.textContent = "Todos los caracteres deben ser números"
                                successfulInput = false
                                e.preventDefault()
                            } 
                        }
                    }else{
                        formElementError.textContent ="Longitud de número telfónico no válido"
                        successfulInput = false
                        e.preventDefault()
                    }
                break


                case 'DNI':
                    if (formElementInput.value.length == 9){ 
                        if (!formElementInput.value[8].match(/[A-Z]/i)){    
                            formElementError.textContent = "El último cáracter del DNI debe ser una letra mayúscula"
                            successfulInput = false
                            e.preventDefault()
                        }else{
                            for (let i = 0; i < formElementInput.value.length - 1; i++){
                                if (!(formElementInput.value[i] >= '0' && formElementInput.value[i] <= '9')){    
                                    formElementError.textContent = "Los primeros 8 caracteres deben ser números"
                                    successfulInput = false
                                    e.preventDefault()
                                } 
                            }
                        }
                    }else{
                        formElementError.textContent = "Tamaño de DNI no válido"
                        successfulInput = false
                        e.preventDefault()
                    }
                break
            }
        }
    }

    formElementError = formCheckBox.querySelector(".register--error")
    if (formCheckBoxInput[0].checked == false){
        formElementError.textContent = "Debes aceptar los terminos y condiciones"
        e.preventDefault()
        successfulInput = false
    } else {
        formElementError.textContent = ""
    }
    
    if (successfulInput){
        for (let i = 0; i < formElements.length; i++){
            formElement = formElements[i]
            formElementInput = formElement.querySelector(".register--input")
            localStorage.setItem(formElement.id, formElementInput.value)
        }
    }
})
let postButton = document.querySelector('.design-btn')
let overlayDiv = document.querySelector('.overlay')

postButton.addEventListener('click', () => {
    overlayDiv.style.display = 'flex'
})

function addLinkField() {
    const wrapper = document.getElementById('links-wrapper') 
    const input = document.createElement('input') 
    input.type = 'url' 
    input.name = 'links' 
    input.className = 'form-control' 
    input.placeholder = 'Введіть посилання' 
    wrapper.appendChild(input) 
}

function addTagField() {
    const wrapper = document.getElementById('tag-inputs-wrapper') 
    const input = document.createElement('input') 

    input.type = 'text' 
    input.name = 'tags' 
    input.placeholder = 'Додайте тег до публікації' 
    input.className = 'form-control' 

    wrapper.appendChild(input) 
}

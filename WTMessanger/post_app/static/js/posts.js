const designPostButton = document.querySelector('.design-btn')

const popUpOverlay = document.querySelector('.overlay')
const postCenterDiv = document.querySelector('.center-div')
const postForm = document.querySelector('.form-create-post')

const closeButton = document.querySelector('.close-popup')

const postContent = document.getElementById('id_content')
const tagButtons = document.querySelectorAll('.add-basic-tag')
const tagInputsWrapper = document.getElementById('tag-inputs-wrapper')
const addTagButton = document.getElementById('add-tag-button')

const linksWrapper = document.getElementById('links-wrapper')
const addLinkButton = document.getElementById('add-link-button')
const imageUploadInput = document.getElementById('image-upload')
const contentWrapper = document.getElementById('content-wrapper')

const imgWrapper = document.getElementById('preview-img-wrapper')

const textArea = document.getElementById('post-text-area')

const likePostBtn = document.getElementById('like-post')
const likesAmount = document.getElementById('likes-amount')

const editPost = document.getElementById('edit-post')

designPostButton.addEventListener('click', () => {
    popUpOverlay.classList.add('active')
    postCenterDiv.classList.add('active')
    postForm.classList.add('active')

    console.log('content added')
    console.log(postContent.value)
    postContent.value = postContent.value.trim() + ' ' + textArea.value.trim()

    console.log('Кнопка натиснута, форма змінює стиль')
})

closeButton.addEventListener('click', () => {
    popUpOverlay.classList.remove('active')
    postCenterDiv.classList.remove('active')
    postForm.classList.remove('active')
    postForm.reset()
    console.log('Закрити форму натиснуто, стиль форми скинуто')
})

tagButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const tagText = btn.textContent.trim()
        if (!postContent.value.includes(tagText)) {
            postContent.value = postContent.value.trim() + ' ' + tagText
            console.log(`Тег "${tagText}" додано до контенту.`)
            // tagText.classList.add('add-basic-tag')
        }
    })
})


addTagButton.addEventListener('click', () => {
    const input = document.createElement('input')
    input.type = 'text'
    input.placeholder = 'Додайте тег до публікації'
    input.className = 'form-control'
    input.name = 'custom_tags'
    tagInputsWrapper.appendChild(input)

    input.addEventListener('blur', () => {
        if (input.value.trim()) {
            const tag = '#' + input.value.trim().replace(/\s+/g, '')
            if (!postContent.value.includes(tag)) {
                postContent.value = postContent.value.trim() + ' ' + tag
            }
        }
        input.remove()
    })
        input.focus()
})

addLinkButton.addEventListener('click', () => {
    const newInput = document.createElement('input')
    newInput.type = 'url'
    newInput.name = 'links'
    newInput.className = 'form-control'
    newInput.placeholder = 'Введіть посилання'

    linksWrapper.appendChild(newInput)
    newInput.focus()
})

imageUploadInput.addEventListener('change', () => {
    const files = imageUploadInput.files
    if (files.length > 0) {
        for (let i = 0; i < files.length; i++) {
            const file = files[i]

            const reader = new FileReader()
            reader.onload = function(e) {

                const wrapper = document.createElement('div')
                wrapper.className = 'image-preview-block'

                const imgPreview = document.createElement('img')
                imgPreview.src = e.target.result
                imgPreview.className = 'preview-img'

                const deleteBtn = document.createElement('button')
                const binImage = document.createElement('img')

                binImage.src = '/static/images/delete_bin.svg'

                deleteBtn.appendChild(binImage)
                deleteBtn.className = 'delete-image-btn'

                deleteBtn.addEventListener('click', () => {
                    wrapper.remove()
                })

                wrapper.appendChild(imgPreview)
                wrapper.appendChild(deleteBtn)
                imgWrapper.appendChild(wrapper)
            }
            reader.readAsDataURL(file)
        }
    }
})


likePostBtn.addEventListener('click', () => {
    console.log('added like')
    likesAmount.textContent ++
})

    // При сабміті форми зібрати всі кастомні теги і посилання в відповідні поля
postForm.addEventListener('submit', (e) => {
    console.log('post was succssesfully saved ')
    console.log(e)
        // Зберігаємо всі кастомні теги (хоча ми вже додали їх у контент)
        // Можна додатково обробити, якщо треба.

        // Збираємо всі посилання у hidden поля (або можна просто лишити input з однаковим name)
        // Django з FormSet не робиться, тому краще залишити всі інпути з однаковим name="links".
})


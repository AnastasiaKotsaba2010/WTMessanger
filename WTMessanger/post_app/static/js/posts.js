const designPostButton = document.querySelector('.design-btn')

const popUpOverlay = document.querySelector('.overlay')
const postCenterDiv = document.querySelector('.center-div')
const postForm = document.querySelector('.form-create-post')

const closeButton = document.querySelector('.close-popup')

designPostButton.addEventListener('click', () => {
    popUpOverlay.classList.add('active')
    postCenterDiv.classList.add('active')
    postForm.classList.add('active')
    console.log('Кнопка натиснута, форма змінює стиль')
})

closeButton.addEventListener('click', () => {
    popUpOverlay.classList.remove('active')
    postCenterDiv.classList.remove('active')
    postForm.classList.remove('active')
    console.log('Закрити форму натиснуто, стиль форми скинуто')
})


// document.addEventListener('DOMContentLoaded', () => {
//     const postContent = document.getElementById('id_content')
//     const tagButtons = document.querySelectorAll('.add-basic-tag')
//     const tagInputsWrapper = document.getElementById('tag-inputs-wrapper')
//     const addTagButton = document.getElementById('add-tag-button')
//     const linksWrapper = document.getElementById('links-wrapper')
//     const addLinkButton = document.getElementById('add-link-button')
//     const imageUploadInput = document.getElementById('image-upload')
//     const contentWrapper = document.getElementById('content-wrapper')
//     const postForm = document.getElementById('post-form')

//     // 

//     // При натисканні на тег-кнопку додаємо тег в кінець контенту
//     tagButtons.forEach(btn => {
//         btn.addEventListener('click', () => {
//             const tagText = btn.textContent.trim()
//             if (!postContent.value.includes(tagText)) {
//                 postContent.value = postContent.value.trim() + ' ' + tagText
//             }
//         })
//     })



//     // Додаємо поле для власного тегу
//     addTagButton.addEventListener('click', () => {
//         const input = document.createElement('input')
//         input.type = 'text'
//         input.placeholder = 'Додайте тег до публікації'
//         input.className = 'form-control'
//         input.name = 'custom_tags'
//         tagInputsWrapper.appendChild(input)

//         // Коли користувач виходить з фокусу, додаємо тег до контенту і прибираємо інпут
//         input.addEventListener('blur', () => {
//             if (input.value.trim()) {
//                 const tag = '#' + input.value.trim().replace(/\s+/g, '')
//                 if (!postContent.value.includes(tag)) {
//                     postContent.value = postContent.value.trim() + ' ' + tag
//                 }
//             }
//             input.remove()
//         })
//         input.focus()
//     })

//     // Додаємо нове поле посилання
//     addLinkButton.addEventListener('click', () => {
//         const newInput = document.createElement('input')
//         newInput.type = 'url'
//         newInput.name = 'links'
//         newInput.className = 'form-control'
//         newInput.placeholder = 'Введіть посилання'
//         linksWrapper.appendChild(newInput)
//         newInput.focus()
//     })

//     // Додаємо вибрані картинки безпосередньо після контенту (у вигляді превʼю)
//     imageUploadInput.addEventListener('change', () => {
//         const files = imageUploadInput.files
//         if (files.length > 0) {
//             for (let i = 0; i < files.length; i++) {
//                 const file = files[i]


//                 // Створюємо превʼю зображення
//                 const reader = new FileReader()
//                 reader.onload = function(e) {
//                     const imgPreview = document.createElement('img')
//                     imgPreview.src = e.target.result
//                     imgPreview.style.maxWidth = '150px'
//                     imgPreview.style.margin = '10px 10px 0 0'
//                     contentWrapper.appendChild(imgPreview)
//                 }
//                 reader.readAsDataURL(file)
//             }
//         }
//     })

//     // При сабміті форми зібрати всі кастомні теги і посилання в відповідні поля
//     postForm.addEventListener('submit', (e) => {
//         // Зберігаємо всі кастомні теги (хоча ми вже додали їх у контент)
//         // Можна додатково обробити, якщо треба.

//         // Збираємо всі посилання у hidden поля (або можна просто лишити input з однаковим name)
//         // Django з FormSet не робиться, тому краще залишити всі інпути з однаковим name="links".
//     })
// })

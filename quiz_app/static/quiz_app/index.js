console.log('index.js')
console.log('hii!')

const url = window.location.href
const modalBtns = [...document.getElementsByClassName('modal-btn')]
const modalBody = document.getElementById('modal-body-data')
const startBtn = document.getElementById('start-quiz')

modalBtns.forEach( modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk')
    const title = modalBtn.getAttribute('data-title')
    const num = modalBtn.getAttribute('data-numquest')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div>
            <p>Are you sure you wanna begin <b>${title}</b>?</p>
            <ul class="text-muted">
            <li> course title: <b>${title}</b></li>
            <li>number of questions: <b>${num}</b> </li>
            <li>duration: <b>${time} min</b> </li>

          </ul>           
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
        // console.log(pk)
    })
}))
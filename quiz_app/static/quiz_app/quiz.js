// console.log('hello world!')

const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
// const timerBox = document.getElementById('timer-box')

// const activateTimer = (time) => {
//     if (time.toString().length < 2){
//         timerBox.innerHTML = `<b>0${time}:00</b>`
//     }else {
//         timerBox.innerHTML = `<b>${time}:00</b>`

//     }

//     let minutes = time - 1
//     let seconds = 60
//     let displaySeconds
//     let displayMinutes


//     const timer = setInterval(() => {
//         seconds--;
//         if (seconds < 0) {
//             seconds = 59
//             minutes--;
//         }
//         if (minutes.toString().length < 2){
//             displayMinutes = '0'+ minutes
//         } else {
//             displayMinutes = minutes
//         }

//         if (seconds.toString().length < 2){
//             displaySeconds = '0' + seconds
//         } else {
//             displaySeconds = seconds
//         }
//         if (minutes === 0 && seconds === 0 ){
//             clearInterval(timer)
//             alert('time over')
//             sendData()
//         }
//         timerBox.innerHTML = `${displayMinutes}:${displaySeconds}`
//     }, 1000)
// }



// gets the questions using ajax
$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: (response) => {
    const data = response.data
    data.forEach(el => {
        for (const [question, answers] of Object.entries(el)){
            quizBox.innerHTML += `
                <hr>
                <div class="quest">
                    <b>${question}</b>                                  
                </div>
            `
            answers.forEach(answer => {
                quizBox.innerHTML += `    
                    <div>
                    <input type="radio" id="ans_${answer}" class="ans" name="${question}" value="${answer}">
                    <label for="ans_${answer}">${answer}</label><br>
                    </div>

                `
            })
        }
    });
    // activateTimer(response.time) //timer
    },  
    error: (error) => {
            console.log(error)
    }
})
// end


const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


// function that sends the data gotten from the options picked
const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].defaultValue
    elements.forEach(el => {
        if (el.checked){
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    // ajax post request
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            quizForm.classList.add('not-visible')
            // console.log(results)
            // console.log(response.score)

            scoreBox.innerHTML += `
               <p>score: <b> ${response.score.toFixed(2)}% </b></p>
            `

            results.forEach(response => {
                const resDiv = document.createElement('div')
                // console.log(response)
                for(const[question, res] of Object.entries(response)){
                    resDiv.innerHTML += `<p>${question}</p>`
                    const cls = ['container', 'p-3', 'text-light','mb-2']
                    resDiv.classList.add(...cls)

                    const selected_answer = res['answered']
                    const correct_answer = res['correct_answer']

                    if (selected_answer == correct_answer){
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML += `answer: ${selected_answer}`     
                    } else {
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML += `<p><i class ="text-info">selected:</i> ${selected_answer || 'none'}</p>`
                        resDiv.innerHTML += `<p class="text-warning"><i class="text-info">correct answer:</i> ${correct_answer}</p>`   
                    }
                }
                
                resultBox.append(resDiv)
            })
        },
        error: function(err){
            console.log(err)
        }
    })


}

quizForm.addEventListener('submit', el => {
    el.preventDefault()

    sendData()
})



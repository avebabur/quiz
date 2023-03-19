const url = window.location.href
const startBtn = [...document.getElementsByClassName('start-button')]
startBtn.forEach(element => {
    element.addEventListener('click', ()=>{
        window.location.href = url + 'quiz/'
    })    
});


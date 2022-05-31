
let cards = []
let sum = 0
let hasBlackJack = false
let isAlive = false
let message = ""
let messageEl = document.getElementById("message-el")
sumEl = document.getElementById("sum-el")
cardEl = document.getElementById("card")

playerEl = document.getElementById("player-el")
let player = {
    name : 'benedore',
    price : 140
}
playerEl.textContent =player.name+ ":" + 0




function getRandomNumber(){
    let randomNumber = Math.floor(Math.random() * 13) + 1
    if(randomNumber === 1){
        return 11
    }
    else if( randomNumber > 10){
        return 10
    }
    else{ 
        return randomNumber
    }

}
function startGame(){
    isAlive=true
    let firstCard = getRandomNumber()
    let secondCard = getRandomNumber()
    let cards = [firstCard, secondCard]
let sum = cards[0] + cards[1]
    renderGame()
}

function renderGame(){
    
    if(sum < 21){
        message = 'do you want to draw a new card'
    }else if(sum === 21 ) {
        message = "your have won"
        hasBlackJack = true
        
        
        playerEl.textContent = player.name + " $" +player.price
    } else {
        message = "you just lost the game"
        isAlive = false
    }
    messageEl.textContent = message
    sumEl.textContent = "Sum: " + sum
    cardEl.textContent = "Cards: " 

    for (let i = 0; i< cards.length; i++) {
        cardEl.textContent += cards[i] + " "
    }

}


function newCard(){
    if(isAlive & sum !=21 ){
        let card = getRandomNumber()
        sum += card

        cards.push(card)
        

        renderGame()
    }
    else{
        return sum
    }
    
}

// for (let i = 10; i <=100; i += 10){
//     console.log(i)
// }

// messages = [
//     'blessed',
//     'benedore',
//     'benedict',
//     'shelia',
//     'bella'
// ]

// for (let m = 0; m < messages.length; m += 1){
//     console.log(messages[m])
// }

// let sentence = ['hello', 'my', 'name ', 'is ', 'benedore ']

// let greetingEl = document.getElementById("greeting-el")

// for (s = 0; s < sentence.length; s ++ ){
//     greetingEl.textContent += sentence[s] + " "
    
// }




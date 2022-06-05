
let hands = ['rock', 'paper', 'scissors']
let len = hands.length

function getHand(){
    let randomNumber =Math.floor( Math.random() * len)

    console.log(hands[randomNumber])
     
}

getHand()

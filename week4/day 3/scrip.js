
   let gameRounds = 0


   function palyTheGame(){
       let play=confirm("are you want to play a game?")
       if (!play){
           alert("ok have a good day")
       } else{
           alert("lets party")
           let num = prompt("please pick a number between 0 and 10")
           if (isNaN(num)){
               alert("you didnt enter a number!!! Goodbye")
               return
           }else if(num>10){
               alert("the nummber you enter is greatrer then 0-10. Goodbye")
           }else{
               let compuerNumber = Math.floor(Math.random()*11);
               test (num,compuerNumber)
           }
       }
   }

function test (num,compuerNumber){
    gameRounds++
    if(gameRounds>3){
        return alert(`the computerNumber # was ` $())
    }
}






// Exercise 1: Simple If/Else Statement
// Instructions
// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.

let x = prompt ('please enter a number');
let y = prompt('please enter the second number');
if ( x > y){
    console.log("x is  biger then y");
} else if( x < y){
    console.log('y is biger then x');
}

// Exercise 2: Chihuahua
// Instructions
// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

let newDog = "Chihuahua"
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLocaleLowerCase());
console.log(newDog ==="Chihuahua")
let favoritDodBread = prompt(" what is your favorit dog bread ");
if ( favoritDodBread == newDog ){
    console.log("I love Chihuahuas, it’s my favorite dog breed?");
} else  {
    console.log("I dont care, I prefer cats");
}


// Exercise 3: Even Or Odd
// Instructions
// Prompt the user for a number and save it to a variable.
// Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.

let userNummber = prompt('please enter your nummber?');
//check if the number is even
if (userNummber % 2 == 0){
    console.log("The number is even");
}
// if the number is odd
else {
    console.log("The number is odd.");
}


// Exercise 4: Group Chat
// Instructions
// Below is an array of users that are online in a group chat.

// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
// Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display:

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
console.log(users)
if(users.length=[]){
    console.log("the users array is empty")
} else if("Lea123"){
    console.log("Lea123 are online");
} 
if (users.length=2){
console.log("Lea123 Princess45 are online");
}
if(users.length=3){
    console.log("Lea123 Princess45 and more are online");
}
// 
// 
// 
// 
// 


// Exercises XP GOLD




// Exercise 1 : The World Translator
// Instructions
// Hint: Use Switch Case

// Ask the user which language they speak.

// Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”

// Create a few conditions :
// If the user speaks French : display “Bonjour”
// If the user speaks English : display “Hello”
// If the user speaks Hebrew : display “Shalom”
// If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’

let language = prompt ( "what language are you speek my friend?" )
if (language == "English"){
    alert ("hello")
} else if (language == "French"){
    alert  ("Bonjour")
}else if (language== "Hebrew" ){
    alert  ("“Shalom”")  
} else if (language!=="Hebrew","French","English" ){
    alert (01110011);
}

// Exercise 2 : The Grade Assigner
// Instructions
// Ask the user for their grade.

// If the grade is bigger than 90, console.log “A”

// If the grade is between 80 and 90 (included), console.log “B”
// If the grade is between 70(included) and 80 (included), console.log “C”
// If the grade is lower than 70, console.log “D

let grade = prompt ( "please enter your grade")
if (grade > 90){
    console.log ("A")
} else if (grade>=80 && grade<=90){
    console.log ("B")
} else if (grade >=70 && grade<=80){
    console.log ("C")
} else if (grade<70){
    console.log ("D")
}




// Daily Challenge: Not Bad
// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.
// Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).
// Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).
// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.

let sentence = "The movie is not that bad, I like it"
let wordNot  = "not"
let wordBad  = "bad"
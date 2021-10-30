// Exercise 1
// Make a keyless car!

// This car will only let you drive if you are over 18. Make it do the following:

// Using prompt() and alert(), ask a user for their age.

// IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
// IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
// IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"

let driversAge = prompt("please enter your age to activatit the car"); 
if (driversAge < 18){
      alert ("sorry but your to young to drive");
} else if (driversAge == 18){
    alert ("Congratulations on your first year of driving. Enjoy the ride!");
} else if (driversAge > 18){
   alert("Powering On. Enjoy the ride!");
}

let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );     
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
    // the code will end in line 29 because case 4 is the correct answer
}


// Exercise 1
// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".

let userName = "fltsputnik177"
let password = 12456789
let database =  [userName,password]
console.log(database)
let newsfeed = (database +" "+password+" " +userName)
console.log(newsfeed);
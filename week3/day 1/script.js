//Exercise 1
// Create a structured HTML file linked to a JS file

// 1. Create these variables and give them values:

// addressNumber
// addressStreet
// country
// 2. Write a variable named globalAddress, and concatenate inside, the variables:

// addressNumber
// addressStreet
// country
// In order to create a sentence
// 3. Display globalAddress Example: globalAddress should display « I live in BenYehuda 5, in Israel »
let adressNumber = 71
let adressStreet = ' even gvirol'
let country = ' israel'

let globalAddress = (adressNumber + adressStreet + country)
console.log(globalAddress);




//Exercise 2
// 1. Store your birth year in a variable.

// 2. Store a future year in a variable.

// 3. Calculate your possible ages for that year based on the stored values.

// 4. Display : "I will be NN in YYYY", substituting the values.
let myAge = 25
let myFuterAge = 30
let differenceInAge = myFuterAge - myAge
console.log(differenceInAge);




//Exercise 3
// 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

// 2. Display dog

// 3. Add to the array pets, the pet horse. Remove the pet rabbit

// 4. Display the array length
let pets = ['dogs','cats','parots','fish','cow','rabbit']
console.log(pets[0]);
pets.push('horse');
pets.pop('rabbit')
console.log(pets);
console.log(pets.length);

// let age = prompt('How old are you?', 20);
// alert(`You are ${age} years old!`);
// let isBoss = confirm("Are you the boss?");
// alert(isBoss);
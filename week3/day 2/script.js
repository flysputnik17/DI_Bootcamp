// Exercise 1 : Guess The Answers
// Guess the correct outcome to the lines of code written below.
// After guessing the outcome check the results of the code below.
// Check them by copying line by line and running them in the console.
    5 + "34"
    5 - "4"
    10 % 5
    5 % 10
    "Java" + "Script"
    " " + " "
    " " + 0 
    true + true
    true + false
    false + true
    false - true
    3 - 4
    "Bob" - "bill"

//     Exercise 1 : Favorite Color
// Instructions
// let me = ["my","favorite","color","is","blue"]

// Write some simple Javascript code that will join all the items in the array above, and console.log the result.
// let me =["my","favorite","color","is","blue"]
// console.log(me);





// Exercise 2 : Mixup
// Instructions
// Create 2 variables. The values should be strings. For example:
// let str1 = "mix" let str2 = "pod"
// Slice out and swap the first 2 characters of the 2 strings from part 1.
// Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
// Finally console.log the new concatenated string.

let str1 = "hello "
let str2 = "world" 
console.log(str1,str2);
 let str3 = str1.slice(0,2)+str2.slice(2,5) +str1.slice(3,5)+str2.slice(0,3)
 console.log(str3);




// Exercise 3 : Calculator
// Instructions
// Make a Calculator. Follow the instructions:

// Prompt the user for the first number.
// Store the first number in a variable called num1.
// Prompt the user for the second number.
// Store the second number in a variable called num2.
// Create an Alert where the value is the SUM of num1 and num2.
// BONUS: Make a program that can subtract, multiply, and also divide!le
// let num1 = prompt ('Enter first nimber');
// let num2 = prompt('Enter second number');
// let sum = Number(num1)+Number(num2);
// alert( 'this is your sum'+ sum);



// Exercise 1 : Find Nemo
// Instructions
// Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo !"
// Find the word “Nemo”
// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]!".
// Bonus : If you can’t find Nemo, console.log “I can’t find Nemo”.
// Hint : use an if/else statement

let name = "Nemo"
let fishName = prompt(" what is your fevorit dinsy fish movie?")
if (fishName === 'Nemo') {
    alert ( 'i found Nemo');
} else {
    alert (" didnt find Nemo")
}
console.log(fishName);



// Daily challenge
// Exercise 1:
// Using this array :

// let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// Remove Banana from the array.
// Sort the array in alphabetical order.
// Add “Kiwi” to the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in part 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// At the end you should see this outcome:

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits . shift() 
fruits.sort();
fruits.push('Kiwi');
fruits. shift();
fruits.reverse();
console.log(fruits);

// Exercise 2:
// Using this array :

// let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// Access and then console.log “Oranges”.
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);
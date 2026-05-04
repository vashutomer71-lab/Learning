// // Loop & Strings

// /* For loop-->A for loop in JS is used to repeat a block of code 
// a specific number of times. It’s one of the most common ways to 
// iterate (loop) through data.------ 
// Syntax for(initialization; stop condation, updation/increment)*/


// for (let i=1; i<=100; i++)
// {
//     console.log("Vashu Tomer"); // block of code
//     // console.log("Priyank Pundir");
// }
// console.log("Loop has ended");

// // Calculate sum of 1 to 5 numbers

// let sum=0;
// for(i=1;i<=5;i++)
// {
//     sum = sum+i;
//     // console.log("The sum of 1 to 5 number is:", sum)
// }
// console.log("The sum of 1 to 5 number is:", sum)


// // Calculate sum of 1 to n numbers

// let sum1=0;
// let n =100;
// for (i=1; i<=n; i++)
// {
//     sum1=sum1+i;
//     console.log("value of i is:", i)
// }
// console.log("Value of 1 to n number is:", sum1)

// // Infinite loop--> Never end the loop because the never condatgion if false, it's always true

//  /* While loop-->  Syntax-- while(stoping condation){do some work}*/

// let i = 1;
// while(i<=10)
//     {
//         console.log("Vashu Tomer");
//         i++;
//     }


// /* do while loop--syntax --> do{//do some work}while(condation) In do while loop at least one time code run
//  and provide output based on condation*/
// let i=1;
// do{console.log("the value is");
//     i++;
// }while(i<=10)

// /* for-of loop --> for of loop is used to itrate the object like:
//  string, array, maps, set. It gives the value automaticaly*/
// str="Vashu Tomer"
// let size=0
//  for(let strval of str){console.log("val:", strval);size++}
//  console.log("String size:",size)
//  // Array example
//  let arvalue=[10,20,30]
//  for(let val of arvalue)
//     {
//         console.log("The value of array is:", val)
//     }

//  /*for-in lopp-->It is used to iterate over the keys (property names)
//   of an object. AND syntax is-> for (let key in object) {// code using key}*/


// let student={
//     firstname:"Vashu",
//     age :31,
//     degination: "SSE",
//     cgpa: 7,
//     isworking: true
// }  
// for(let key in student)
//     {
//         console.log("key: ",key)
//     }


// // Practice Question-> Print all the Even number 0 to 100
// let num=0
// for(let num=1; num<=100; num++)
// {
//     // console.log("The value of i is :", num)
//     if(num%2===0)
//     console.log("The even number is:", num)
//     if(num%2!==0)
//     console.log("The number is not even:", num)
// }

/*Q2-- Create a game where you start any random game number. 
Ask the user to keep guessing the game number untill the user 
enters correct value.*/
// let gamenum =26;
// let usernumber=prompt("User Gusee the number is:")
// while(usernumber !=gamenum)
//     {
//      console.log("You enter wrong number. Gusee again");
//     }
// console.log("Congrulation you enter correct number:",usernumber);



/* Strings--> String is a sequence of characters used to represent text */

let string ="Vashu Tomer"; //create a string using double quotes
let string2='Vashu Tomer'; //create a string using single quotes

/* string length--> The length of a string is the number of 
characters it contains, including spaces and punctuation. 
You can find the length of a string using the .length property.*/
console.log(string.length);

/* String indexing--> Each character in a string has a position, 
called an index. The first character is at index 0, the second 
at index 1, and so on. You can access individual characters in a 
string using their index.*/
console.log(string[0])
console.log(string[3])

/* Template Literals--> Template literals are a way to create strings 
in JS that allow for easier string interpolation and 
multi-line strings. They are enclosed in backticks (`) instead of 
single or double quotes. Template literals can contain placeholders,
 which are denoted by ${expression}. The expression inside the 
 placeholder is evaluated and its result is included in the string.*/

 let string3=`Vashu Tomer`; //create a string using backticks/Template Literals

console.log(string3)

let obj ={
    item: "pen",
    price: 10
}

console.log("The price of ", obj.item,  "is",  obj.price , "dollars.")
let str = `The price of ${obj.item} is ${obj.price} rupees.`;
console.log(str)

/* Escape Characters--> Escape characters are special characters that 
are used to represent certain characters in a string that would 
otherwise be difficult to include. They are denoted by a backslash (\)
 followed by the character you want to include. For example, 
 if you want to include a double quote in a string that is enclosed
  in double quotes, you can use the escape character like this: 
"This is a \"quote\"." This will output: This is a "quote".*/

let str1 = "Vashu Tomer\n is a good girl"; // \n is used to create a new line in the string
console.log(str1)

let str2 = "Vashu Tomer\t is a good girl"; // \t is used to create a tab in the string
console.log(str2)
console.log(str2.length) // \t is considered as one character in the string


/* String Methods--> String methods are built-in functions that allow 
you to manipulate and work with strings in JS. Some common string
methods include:
- .toUpperCase(): Converts a string to uppercase letters.
- .toLowerCase(): Converts a string to lowercase letters.
- .trim(): Removes whitespace from both ends of a string.
- .slice(): Extracts a section of a string and returns it as a new string.
.concat(): Combines two or more strings into one string.
.replace(): Replaces a specified value with another value in a string.
charatAt(): Returns the character at a specified index in a string.
*/
let str3 = "   Vashu Tomer   ";
console.log(str3.trim()) // it will remove the white space from both end of the string
console.log("The Trimed value is:",str3.trim().length) // it will give the length of the string after removing the white space from both end of the string 
console.log("The Uppercase value is:", str3.toUpperCase()) // it will convert the string to uppercase letters
console.log("The Lowercase value is:", str3.toLowerCase()) // it will convert the string to lowercase letters

/*NOTE: It is not change the original string because string is 
immutable in JS, it will return a new string with the changes.*/

let str4 = "Piku";
let newstr=str4.toUpperCase();
console.log(str4) // it will give the original string because string is immutable in JS, it will return a new string with the changes.
console.log(newstr) // it will give the new string with the changes.

let str5 = "Vashu Tomer";
console.log(str5.slice(0,5)) // it will extract the section of the string from index 0 to index 4 and return it as a new string.
console.log(str5.slice(6)) // it will extract the section of the string from index 6 to the end of the string and return it as a new string.

let str6 = "Vashu Tomer";
console.log(str6.replace("Vashu", "Priyank")) // it will replace the specified value "Vashu" with another value "Priyank" in the string and return a new string.
console.log(str6) // it will give the original string because string is immutable in JS, it will return a new string with the changes.

let str7 = "Vashu Tomer";
console.log(str7.charAt(0)) // it will return the character at index 0 in the string.
console.log(str7.charAt(6)) // it will return the character at index 6 in the string.       

let str8 = "Vashu Tomer";
console.log(str8.concat(" is a good girl")) // it will combine the two strings "Vashu Tomer" and "


let    str9 = "Vashu Tomer";
console.log(str9.toLowerCase().replace("vashu", "priyank").concat(" is a good boy")) // it will convert the string to lowercase letters, replace the specified value "vashu" with another value "priyank" in the string and combine the two strings "priyank tomer" and " is a good boy

/*Practice Question--> Prompt the user to enter their full name. 
Generate a username for them based on the input. Strat username with @,
followed by their full name and ending with the fullname lenght.*/

let fullname= prompt("Enter your full name")
console.log(fullname)
let username = "@"+fullname+fullname.length
console.log("Your username is:", username)

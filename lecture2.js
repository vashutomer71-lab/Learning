// // ----------Operations & Conditional Statement-----------
// //========comment------------
// //Comment in JS--- PArt of code which is not executed
// /* this line of code is not executed
// this is not long and multiple line comment*/

// //----------Operations id JS------------

// /* 1 Arthmatic operator---------+,_,*,/,Modules(%), Exponentiation(**),
// Increment(++), Decrement(--)[++,-- are also called unary operator]*/
// let a =4;
// let c=5;
// console.log("The sum of a+c is:",a+c);
// console.log("The sub of a-c is:", a-c);
// console.log("The multiply of a*c is:", a*c);
// console.log("The devide of a/c is:", a/c);
// console.log("The modules value is", a%c);
// console.log("The Exponentiation value is ", a**c)

// console.log("The value of a is:", a)
// //Unary Operators are mentation below
// console.log("The pre incremnt value ++a is: ", ++a) // pre incoremnt
// console.log("The pre decremnt value --a is : ", --a) //pre decremnt
// console.log("The post incremnt value a++ is: ",  a++) // pre, post incoremnt
// console.log("The post decremnt value a-- is: ", a--) //pre & post decremnt
// console.log("The value of a is:", a)
// a= a+1
// console.log("value of a+1 is", a)

// //-----------Assignment operators----- =, +=, -=,*=, %=, **=  -----
// let x=6;
// let y=4;

// // a+=1 means that a=a+1, compact way to write this is a+=1

// // x+=4; // x= x+4

// console.log("The value of a is:",x=x+4)

// // x-=4; // x=x-4
// console.log("The value of x=x-4 is:", x=x-4);
// console.log("The value is x*= is:", x=x*4)

// /* --------------Comparsion Operators------ 
// Eqal to ==, Not Equal to !=, Equal to & type ()===), 
// Not equal to & type (!==) , >, <,<=, >=-----*/

// let a=5;
// let b="2";
// console.log("a==b", a==b); // Befoure compression js convert the string value to number and then compare

// console.log("a!=b", a!=b);
// console.log("a===b", a===b) // === strict compression version
// console.log("a!==b", a!==b) // === strict compression version
// console.log("a<b",a<b)
// console.log("a>b",a>b)

// console.log("a<=b",a<=b)
// console.log("a>=b",a>=b)

// //Logical Operators-------- AND(&&), OR (||), NOT(!)

// let a=6;
// let b=5;
// let cond1= a<b; // true
// let cond2 = a===6 // true
// console.log("cond1 && cond2", cond1 && cond2)
// console.log("cond1 || cond2", cond1||cond2);

// // ----Conditional Statemaents-> TO implament some condation in the code------
// // if statements

// let mode = "dark";
// let colour;
// if(mode==="dark")
// {
//     colour="black";
// }

// if(mode==="light")
// {
//     colour ="white"
// }

// console.log(colour)


//  let age=18;
//  if(age=18)
//     {
//      console.log("You can vote")
//     }
//  if(age =17)
//     {
//      console.log("You can not vote")
//     }   


// //if-else statements
// let mode= "blue"
// let colour;

//  if(mode==="dark")
//  {
//     colour = "Black"
//  }
//  else
//  {
//     colour="White"
//  }
//  console.log(colour)

 // if elseif statement

//  let mode1 = "green";
//  let colour1;
//  if(mode1==="dark")
//    {
//       colour1="Black"
//  }
//  else if(mode1==="green")
//        {colour1="Green"}
//  else if(mode1==="Brown")
//         {colour1="Brown1"}
//  else
//  {
//    colour1="Yellow"
//  }
//  console.log(colour1)

//  // Question---- Get user to input a number using prompt("Enter a number:"). Check if the number is a multiple of 5 or not?

// let num = prompt("Enter a number:")
// if(num%5===0)
// {
//    console.log(num, "The number is a multiple of 5")
// }
// else
//    {
//       console.log(num, "The number is not multiple of 5")
//    }

/* Question No. 2- Write a code which can give grades to students according to there scores:
90-100, A
80-89, B
70-79, C
60-69, D
50-59, E
0-49, F*/

let score = prompt("Value of score:")
// let score=55;
let grade;

if(score>=90 && score<=100){
   grade="A";
}else if(score>=80 && score<=89){
   grade="B";
}else if(score>=70 && score<=79){
   grade="C";
}else if(score>=60 && score>=69){
   grade="D";
}else if(score>=50 && score>=59){
   grade="E";
}else if(score>=0 && score>=49){
   grade="F";
}

console.log("According to your score, your grade was", grade)


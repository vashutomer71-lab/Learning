//Variavles and data types



// console.log('Vashu Tomer want to learn javascript')
// fullName= "Vashu Tomer"
// age= 30
// degination ="SSE"
// x=null
// y=undefined
// isfolowwed=true
// console.log(fullName,age,degination)
// console.log(x)
// console.log(y)
// console.log(isfolowwed)/

//----------- Variable in JS--------------------

// var fullName= "Vashu" // variable can be re-declared & Update. A global scop variable.
// let name = "Vashu Tomer" // variable cannot be re-declared but can be updated. A block scop variable.
// const lastName= "Tomer" // variable cannot be re-declared or updated. A block scop variable.

// var age =30
// var age=40
// var age=50
// console.log(age)

// let age1 =60
// age1 =40
// age1 = 60
// console.log(age1)

// const age2=70
// console.log(age2)

//-----DATA TYPE IN JS-> Primptive & non Primptive(Object)------
//Primptive(7) Data type--> That are fixed--> Number, String, boolean, Undefined, Null, BigInt, Symbol

let age = 80 //number
let str = "Vashu" //string
let ispaid = true //boolean
let x;
let y=null;

let b=BigInt("123")
let s=Symbol("Say Hello")

//----Non Primptine data type----in the object key:value pair data are present in the object

const student = {
    FullName: "Vashu Tomer",
    age: 50,
    presentage: 70,
    isPass: true
}
student["age"] = student["age"]+5; // We can update the const object value but can not update the normal const value
student["name"] = "Vashu Tomer Pundir"
console.log(student);
console.log(student.FullName)
console.log(student["age"]);
console.log(student["name"]);

// Practice Quesyion--- Create the object called product to store the blue ball pen information


const product ={
    title :  "ball pen",
    colour : "black",
    rating : 4.5,
    price : 200,
    isdeal: true,
    offer: 5
}
console.log(product)
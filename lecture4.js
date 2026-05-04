/* Arrays-> Aray is a collection of similar data types. It is a data 
satructurethat can hold more than one vlue at a time. It is an codered
collection of data. It is a non-primtive data type. It is a object in
js. It is a dynamic data structure. It can hold any data type. It can 
hold dplucate values. It is an ordered collection of data. It is a 
zero indexed collection of data. It is a mutable data structure. 
It is a non-primitive data type. It is a object in js. It is a dynamic
data structure. It can hold any data type. It can hold duplicate 
values. It is an ordered collection of data. It is a zero indexed
collection of data. It is a mutable data structure.
*/
let marks =[90,92,86,60,50,40,54,70,78,80,88]
// console.log(marks)
// console.log(marks[0]) // 90 Indices start from 0
// console.log(marks[1]) // 92
// markslength=marks.length // 11
// console.log(markslength)
// for(i=0; i<marks.length; i++)
//     {
//         console.log(marks[i])
//     }


let heroes=["SUPERMAN", "BATMAN", "SPIDERMAN", "IRONMAN", "CAPTAIN AMERICA"]
//print all the heros name using for loop
for(i=0; i<heroes.length; i++)
    {
        console.log(heroes[i])
    }    
 //print all the heros name using for of loop-- mostly used loop
for(let hero of heroes)
    {
        console.log(hero.toLowerCase())
    }

let citys=["Delhi", "Mumbai", "Noida", "Hapur", "Meerut"]
for(let city of citys)
{
    console.log(city.toUpperCase())
}
// print all the heroes name using for in loop-- it is used to print the index of the array
for(let index in heroes)
    {
        console.log(heroes[index])
    }
// Prectice Question-> For a given array with the marks of students->[85,97,44,37,76,60]. Find the average marks of entire class.
let studentMarks=[85,97,44,37,76,60]
//Type 1
let sum=0;
for(let mark of studentMarks){
    sum=sum+mark;
}
let average= sum/studentMarks.length
console.log("The average marks of students using for of loop is:", average)

//Type 2
let studMarks=[85,97,44,37,76,60]
let sum1=0;
for(let i=0;i<studentMarks.length;i++){
    sum1=sum1+studMarks[i];
}
let average1= sum1/studMarks.length
console.log("The average marks of students using for loop is:", average1)

//Type 3
let studMarks1=[85,97,44,37,76,60]
let sum2=0; 
for(let index in studMarks1)
    {
        sum2 += studMarks1[index]
    }
let average2= sum2/studMarks1.length
console.log(`The average marks of students using for in loop is: ${average2}`)

/*Practice Question-> For a given array with prices of 5 itms->
[250,645,300,900,50]. All items have an offer of 10% OFF on them. 
Change the array to store the final price after applying offer.*/
let price =[250,645,300,900,50]

for(let i=0; i<price.length; i++)
{
    offer=price[i]*10/100
    console.log("offer is:", offer)
    newprice=price[i]-offer
    console.log("The final price after applying offer is:", newprice)
    price[i]=newprice
}
console.log("The updated price array is:", price)

let prices =[250,645,300,900,50]
let updatedPrices=[];
for(let price of prices)
{
    offer= price*10/100
    finalprice=price-offer
    updatedPrices.push(finalprice)
}
console.log('The updated "price" array is:', updatedPrices)
console.log("The updated 'price' array is:", updatedPrices)

// Array in JS -> Array Methods

// Push() Add the values at the position of end
let frutis=["Mango", "Banana", "Apple", "Lachhi", "Grapes"]
frutis.push("Watermelon")
console.log(frutis)

// Pop() Remove the values at the position end[remove from end & return]

frutis.pop()
deletedfruit=frutis.pop()
console.log("Deleted fruit is:", deletedfruit)
console.log(frutis)
//toString(): converts array to string
let markss=[90,92,86,60,50,40,54,70,78,80,88]
let newstr= markss.toString()
console.log("The array convert in string", newstr)

// concat() array to string with the given separator
let indianCities=["Delhi", "Mumbai", "Noida", "Hapur", "Meerut"]
let usacitys=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
let cityis=indianCities.concat(usacitys)
console.log("The concat array is:", cityis)

// unshift() → add at beginning
let cityi=["Mumbai", "Noida", "Hapur"]
cityi.unshift("Kolkata"); 
console.log(cityi) // ["Kolkata", "Mumbai", "Noida", "Hapur"]
// shift() → remove from beginning
cityi.shift(); 
console.log(cityi)     // []

//slice(startindex, endindex) → it is used to extract a section of an array and return it as a new array. It does not modify the original array.
let citys1=["Delhi", "Mumbai", "Noida", "Hapur", "Meerut"]
let newcity=citys1.slice(1,4) // it will extract the section of the array from index 1 to index 3 and return it as a new array.
console.log("The new array is:", newcity)
console.log("The original array is:", citys1) // it will give the original array because slice() does not modify the original array.        

//splice(startindex, deleteCount, item1, item2, ...) → it is used to add or remove elements from an array. It modifies the original array.
let citys2=["Delhi", "Mumbai", "Noida", "Hapur", "Meerut"]
citys2.splice(2,1) // it will remove 1 element from index 2 and return it as a new array.
console.log("The new array is:", citys2) // it will give the modified array because splice() modifies the original array.       

/*Practice Questions-> 
Q1- Create an array to store companies - > "Bloomberg", "Microsoft","Uber", "Google", "IBM", "Apple" 
Q2 -  Remove the first company from the array
Q3 Remove Google And add Ola in its place
Q4 Add Amazon at the end     */

let companies = ["Bloomberg", "Microsoft","Uber", "Google", "IBM", "Apple"]
console.log("The first company name is removed from the array:", companies.shift())

let companys = ["Bloomberg", "Microsoft","Uber", "Google", "IBM", "Apple"]

companys.splice(3,1,"Ola") // it will remove 1 element from index 3 and add "Ola" in its place and return it as a new array.
console.log("The modified array is with add ola at place of google:", companys)

let company = ["Bloomberg", "Microsoft","Uber", "Google", "IBM", "Apple"]
console.log("The modified array is with add Amazon at the end:", company.concat("Amazon")) // it will add "Amazon" at the end of the array and return it as a new array. It does not modify the original array.

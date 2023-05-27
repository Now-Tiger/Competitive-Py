#!/usr/bin/env node

type Points = 20 | 30 | 40 | 50 | null;
let score: Points = 20;
// console.log(score);

type ComplexPerson = {
    firstname: string, 
    lastname: string, 
    age: number, 
    address: string | null,
    email: string | null, 
    city: string | null,
    points: Points,
}

let emp1 : ComplexPerson = {
    firstname : "Swapnil",
    lastname : "Narwade",
    age : 26,
    address : "Sinhgad campus",
    email : null,
    city : null,
    points: 50,
}

let emp2 : ComplexPerson = {
    firstname : "Sanket",
    lastname : "Sangale",
    age : 28,
    address : "Sinhgad campus",
    email : "sangle@gmail.com",
    city : "Pune",
    points: null,
}

console.log(emp1.firstname, emp1.lastname, emp1.points);
console.log("--------------------")
console.log(emp2.firstname, emp2.lastname, emp2.points);

// console.log(emp1 + "\t" + emp2)
#!/usr/bin/env node shape.ts
/**
 * @author: Swapnil Narwade
 * @version: 0.1
 * @description: object oriented tutorial.
 */

class Person {
    name: String;
}

const jill: { name : String } = {
    name : "Jill"
};

const person: Person = jill;

console.log(person)
console.log(jill.name)

/*----------------------------------------*/

let obj: { name : string } & { age : number } = {
    name : "Swapnil",
    age : 26,
}
console.log(obj);

/*---------------------------------------------*/


#!/usr/bin/env node
/* ------------- Interface with the class example --------------*/
interface size {
    width: string,
    height: string,
    getwidth(): string,
}

class Shapes implements size {
    width: string;
    height: string;
    constructor(width: string, height: string) {
        this.width = width;
        this.height = height;
    }
    getwidth(): string {
        return this.width;
    }
}
/* ------------------------------------------------------------*/
interface Person {
    name: string,
    age: number,
    address: string | null,
}

function greet(person: Person): string {
    return `Hello ${person.name}`;
}

let pers: Person = {
    name: "Swapnil",
    age: 26,
    address: null,
}

console.log(greet(pers));
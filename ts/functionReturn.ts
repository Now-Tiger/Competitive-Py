#!/usr/bin/env node

function calculate_distance(distance: number) : number {
    return distance + 50;
}

function eat(calories: number) {
    console.log(`I ate ${calories} calories today!`);
}   

function sleepIn(hours: number) : void {
    if (hours <= 8) {
        console.log("I slept well today!");
    } else {
        console.log(`I slept for ${hours} today!!!`);
    }
}

let ate = eat(100);
console.log(ate);

let slept = sleepIn(10);
console.log(slept);

let distance = calculate_distance(50);
console.log(distance);
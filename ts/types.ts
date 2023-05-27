#!/usr/bin/env node shape.ts
/**
 * @author: Swapnil Narwade
 * @version: 0.1
 */

let a: any = 55;
a = "string now";
a = new Array();
a.push(33);

console.log(a)

/*---------------------------*/

let val: unknown = 22;
val = "string value";
val = new Array();

if (val instanceof Array) {
    val.push( 33 );
}

console.log(val);
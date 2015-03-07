[[MDN Arrays|https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array]]
* Create Arrays
{{{
array = [element0, element1, ..., elementN]
array = new Array(element0, element1[, ...[, elementN]])
array = new Array(arrayLength)
var map_array = {
  'item1'  : 'text',
  'array1': [1, 2, 3, 4]
};
}}}
* Accessing
{{{
ferarray.0   // a syntax error
ferarray[0]  // works properly
Object.keys(map_array) // get the keys
}}}
* Appending elements
{{{
var fruits = [];
fruits.push('banana', 'apple', 'peach');
fruits.length // 3
}}}
* Other important methods
{{{
Array.prototype.pop() // Removes the last element from an array and returns that element.
Array.prototype.push() // Adds one or more elements to the end of an array and returns the new length of the array.
Array.prototype.shift() // Removes the first element from an array and returns that element.
Array.prototype.reverse()
Array.prototype.sort()
Array.prototype.concat() // Returns a new array comprised of this array joined with other array(s) and/or value(s).
Array.prototype.includes() // Determines whether an array contains a certain element, returning true or false.
Array.prototype.join() // Joins all elements of an array into a string.
Array.prototype.slice() // Extracts a section of an array and returns a new array.
Array.prototype.toSource() // Returns an array literal representing the specified array.
Array.prototype.toString() // Returns a string representing the array and its elements.
Array.prototype.indexOf() // Returns the first (least) index of an element within the array equal to the specified value, or -1 if none is found.
}}}
* Iteration methods:
# Every:tests whether all elements in the array pass the test implemented by the provided function.
{{{
function isBigEnough(element, index, array) {
  return element >= 10;
}
[12, 5, 8, 130, 44].every(isBigEnough);   // false
[12, 54, 18, 130, 44].every(isBigEnough); // true
}}}
# forEach
{{{
function log(element, index, array) {
  console.log('a' + index ' = ' + element + ',');
}
[2, 5, , 9].forEach(log);  // logs: a0 = 2, a1 = 5, a3 = 9,
}}}
* Map / Reduce
{{{
var numbers = [1, 4, 9];
var roots = numbers.map(Math.sqrt); // roots = [1, 2, 3]
var sum = numbers.reduce(function(previousValue, currentValue, index, array) {
  return previousValue + currentValue;
}); // arr.reduce(callback[, initialValue])
}}}

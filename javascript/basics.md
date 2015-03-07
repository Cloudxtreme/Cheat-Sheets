[[Strings|https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String]]
[[Events|http://www.w3schools.com/tags/ref_eventattributes.asp]]
[[Navigator|http://www.w3schools.com/jsref/obj_navigator.asp]]
[[Element|http://www.w3schools.com/jsref/dom_obj_all.asp]]
[[MDN Operators|https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators]]
! Operators
* delete
{{{
delete objectName;
delete objectName.property;
delete array[index];
delete property; // legal only within a with statement
}}}
* in
{{{
var trees = new Array("redwood", "bay", "cedar", "oak", "maple");
3 in trees;        // returns true
6 in trees;        // returns false
"bay" in trees;    // returns false (specify index number, not value)
"length" in trees; // returns true (length is an Array property)
}}}
* typeof / instanceof
{{{
typeof myFun;     // returns "function"
typeof shape;     // returns "string"
typeof size;      // returns "number"
typeof today;     // returns "object"
typeof dontExist; // returns "undefined"

if (theDay instanceof Date)
}}}


!Strings
{{{
x = 'string';
x.substr(3,3);
console.log(x);
}}}

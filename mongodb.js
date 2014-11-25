show dbs
show collections
show users
show roles

* db.createCollection("users")
* db.users.insert({name: "Bob", age: 32})

db.users.findOne()
db.users.find(FILTER, FIELDS)
db.users.find({}, {name: 1, age: 1, _id:0})
db.users.find({username: "Jones", date: new Date()});
db.users.find({age: 33}, {name: 1, age:1, _id:0})
db.users.find({age: {$gt: 33}})
db.users.find({username: /^Jones/});
db.users.find({"IMAGE URL":{$ne:null}}); 	// IS NOT NULL

db.users.find({age: {$lte: 33}}).sort({username: 1, date: 1}).limit(100)
db.users.count({age: {$lte: 33}}).sort({username: 1, date: 1}).limit(100)

db.users.update(FILTER, SET, {multi: true})
db.users.update({name: "Bob"}, {$set:{age: 33}}, {multi: true})
db.users.update({name: "Bob"}, {$inc:{age: 2}}, {multi: true})

{a: 10, b: "hello"} 			// a=10 AND b="hello".
{a: {$gt: 10}}					// a is greater than 10 "$lt, $gte, $lte, $ne"
{a: {$in: [10, "hello"]}}		// a is either 10 or "hello".
{a: {$all: [10, "hello"]}}		// a is an array containing both 10 and "hello".
{"a.b": 10} 					// a is an embedded document with b equal to 10.
{a: {$elemMatch: {b: 1, c: 2}}}	// a is an array that contains an element with both b equal to 1 and * c equal to 2.
{$or: [{a: 1}, {b: 2}]}			// a is 1 or b is 2.
{a: /^m/}						// a begins with the letter m.
{a: {$mod: [10, 1]}}			// a mod 10 is 1.
{a: {$type: 2}}					// a is a string (see bsonspec.org for more)

{a: {$nin: [10, "hello"]}} 		// a is anything but 10 or "hello".
{a: {$size: 3}} 				// a is an array with exactly 3 elements.
{a: {$exists: true}} 			// Docs containing an a field.
{a: /foo.*bar/} 				// a matches the regular expression foo.*bar.
{a: {$not: {$type: 2}}} 		// a is not a string. $not negates any of the other query operators.

{$inc: {a: 2}} 					// Increment a by 2.
{$set: {a: 5}} 					// Set a = 5.
{$unset: {a: 1}} 				// Delete the akey.
{$push: {a: 1}} 				// Append the value 1to the array a.
{$push: {a: {$each: [1, 2]}}} 	// Append both 1and 2to the array a.
{$addToSet: {a: 1}}				// Append the value 1to the array a(if the value doesn’t  already exist).
{$addToSet: {a: {$each: [1, 2]}}} // Append both 1and 2to the array a(if they don’t already exist).
{$pop: {a: 1}} 					// Remove the last element from the array a.
{$pop: {a: -1}} 				// Remove the first element from the array a.
{$pull: {a: 5}} 				// Remove all occurrences of 5from the array a.
{$pullAll: {a: [5, 6]}} 		// Remove all occurrences of 5or 6from the array a
show dbs
show collections
show users
show roles

* db.createCollection("users")
* db.users.insert({name: "Bob", age: 32})

* db.users.find(FILTER, FIELDS)
* db.users.find({}, {name: 1, age: 1, _id:0})
* db.users.find({username: "Jones", date: new Date()});
* db.users.find({age: 33}, {name: 1, age:1, _id:0})
* db.users.find({age: {$gt: 33}})
* db.users.find({username: /^Jones/});
* db.mycollection.find({"IMAGE URL":{$ne:null}}); // IS NOT NULL

* db.users.find({age: {$lte: 33}}).sort({username: 1, date: 1}).limit(100);
* db.users.count({age: {$lte: 33}}).sort({username: 1, date: 1}).limit(100);

* db.users.update(FILTER, SET, {multi: true})
* db.users.update({name: "Bob"}, {$set:{age: 33}}, {multi: true})
* db.users.update({name: "Bob"}, {$inc:{age: 2}}, {multi: true})

{a: 10, b: "hello"} // Docs where a is 10 and b is "hello".
* `{a: {$gt: 10}}` Docs where a is greater than 10. Also available: `$lt (<), $gte (>=), $lte (<=), and $ne * (!=).`
* `{a: {$in: [10, "hello"]}}` Docs where a is either 10 or "hello".
* `{a: {$all: [10, "hello"]}}` Docs where a is an array containing both 10 and "hello".
* `{"a.b": 10}` Docs where a is an embedded document with b equal to 10.
* `{a: {$elemMatch: {b: 1, c: 2}}}` Docs where a is an array that contains an element with both b equal to 1 and * c equal to 2.
* `{$or: [{a: 1}, {b: 2}]}` Docs where a is 1 or b is 2.
* `{a: /^m/}` Docs where a begins with the letter m.
* `{a: {$mod: [10, 1]}}` Docs where a mod 10 is 1.
* `{a: {$type: 2}}` Docs where a is a string (see bsonspec.org for more)

* {a: {$nin: [10, "hello"]}} Docs where a is anything but 10 or "hello".
* {a: {$size: 3}} Docs where a is an array with exactly 3 elements.
* {a: {$exists: true}} Docs containing an a field.
* {a: /foo.*bar/} Docs where a matches the regular expression foo.*bar.
* {a: {$not: {$type: 2}}} Docs where a is not a string. $not negates any of the
* other query operators.* 
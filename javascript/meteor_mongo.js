Posts.insert({
  createdBy: Meteor.userId(),
  createdAt: new Date(),
  title: "My first post!",
  content: "Today was a good day."
});

Books.insert({
	title: "Ulysses", 
	author: "James Joyce"
}, function(error, result) {
	// error will be defined AND result = undefined or false 
	// List of errors on `error.invalidKeys` or 
	// Books.simpleSchema().namedContext().invalidKeys()
});

var post = Posts.findOne({
  createdBy: "12345",
  title: {$regex: /first/}
});


Posts.update({
  title: {$regex: /first/}
}, {
  $set: {content: "Tomorrow will be a great day."}
});

Books.update(
	book._id, 
	{$unset: {copies: 1}}, 
	function(error, result) {

});

Posts.allow({
  insert: function (userId, post) {
    return post.createdBy === userId;
  },
  remove: function (userId, post) {
    return post.createdBy === userId;
  }
});

Posts.deny({
  insert: function (userId, post) {
    return post.title === "First!";
  }
});

// Accounts
Meteor.users.findOne(Meteor.userId()); // {{ currentUser }}

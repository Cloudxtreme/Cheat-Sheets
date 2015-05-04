<?php
class User extends Eloquent {
    protected $table = 'users';
}

$user = new User;
$user->name = 'John';
$user->save();
$insertedId = $user->id;

$users = User::all();
$model = User::find(1);
$model = User::findOrFail(1);
$model = User::where('votes', '=', 100)->firstOrFail();
$users = User::where('votes', '>', 100)->take(10)->get();

$count = User::where('votes', '>', 100)->count();
$users = User::whereRaw('age > ? and votes = 100', array(25))->get();

$user = User::create(array('name' => 'John'));
$user = User::firstOrCreate(array('name' => 'John'));
$user = User::firstOrNew(array('name' => 'John'));    // instantiate

$user->save(); // update
$user->push(); // with relationships
$user->delete();

# update a set of rows
$affected_rows = User::where('votes', '>', 100)->update(array('status' => 2));

User::destroy(1); // by key
User::destroy(array(1, 2, 3));
User::destroy(1, 2, 3);

$affectedRows = User::where('votes', '>', 100)->delete();
$user->touch(); // update timestamps

// Popular Queries
class User extends Eloquent {
    public function scopePopular($query) {
        return $query->where('votes', '>', 100);
    }
	public function scopeWomen($query) {
        return $query->whereGender('W');
    }
}
$users = User::popular()->women()->orderBy('created_at')->get();

// Relationships One To One
class User extends Eloquent {
    public function phone() {
        return $this->hasOne('Phone');
    }
}
$phone = User::find(1)->phone;

// Relationships One To Many
class Post extends Eloquent {
    public function comments() {
        return $this->hasMany('Comment');
    }
}
$comments = Post::find(1)->comments;
$comments = Post::find(1)->comments()->where('title', '=', 'foo')->first();

// Querying Relations When Selecting
$posts = Post::has('comments')->get();
$posts = Post::has('comments', '>=', 3)->get();
$posts = Post::whereHas('comments', function($q) {
    $q->where('content', 'like', 'foo%');
})->get();

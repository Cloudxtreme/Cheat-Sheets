```
php -r "readfile('https://getcomposer.org/installer');" | php
echo @php "%~dp0composer.phar" %*>composer.bat
composer -V

composer install --dev

```
== Database
```
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

class User extends Eloquent {
    protected $table = 'users';
}
$users = User::all();
$user = User::find(1);
$user->name
$model = User::findOrFail(1);
$model = User::where('votes', '>', 100)->firstOrFail();
$users = User::where('votes', '>', 100)->take(10)->get();

$count = User::where('votes', '>', 100)->count();
$users = User::whereRaw('age > ? and votes = 100', array(25))->get();

$user = new User;
$user->name = 'John';
$user->save();
$insertedId = $user->id;

$user = User::create(array('name' => 'John'));
$user = User::firstOrCreate(array('name' => 'John'));
$user = User::firstOrNew(array('name' => 'John'));    // instantiate


$user = User::find(1);
$user->email = 'john@foo.com';
$user->save();

$user->push(); // with relationships
$user->delete(); 
User::destroy(1); // by key
User::destroy(array(1, 2, 3));
User::destroy(1, 2, 3);
$affectedRows = User::where('votes', '>', 100)->delete();

$user->touch(); // update timestamps

created_at
updated_at
```

== Popular Queries
```
class User extends Eloquent {
    public function scopePopular($query) {
        return $query->where('votes', '>', 100);
    }
	public function scopeWomen($query) {
        return $query->whereGender('W');
    }
}
$users = User::popular()->women()->orderBy('created_at')->get();
```

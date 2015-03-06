php -r "readfile('https://getcomposer.org/installer');" | php
echo @php "%~dp0composer.phar" %*>composer.bat
composer -V

composer install --dev

== Database
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

<migrations>
  php artisan make:migration create_users_table
  php artisan make:migration add_votes_to_user_table --table=users
  php artisan migrate
  php artisan migrate --force
  php artisan migrate:rollback
  php artisan migrate:reset
</migrations>

<?php
/*
 *  Models
 */
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

$user->push(); // with relationships
$user->delete(); 
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

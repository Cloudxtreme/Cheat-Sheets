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

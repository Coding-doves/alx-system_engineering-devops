# Using strace, find out why Apache is returning a 500 error

file_line { 'fix-wordpress':
  path    => '/var/www/html/wp-settings.php',
  line    => 'define("phpp", "php");',
  match   => '^define\("phpp", "php"\);',
  ensure  => present,
  require => File['/var/www/html/wp-settings.php'],
}

# fix apache web setings and then automate it using Puppet.

exec { 'fix_apache_setting':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

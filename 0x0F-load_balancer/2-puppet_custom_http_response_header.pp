# creating a custom HTTP header response
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}
# instailling nginx
package { 'nginx':
  ensure => installed,
}

# creating a ninx confiuration file
file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-avaliable/default',
  line   => "\tadd_header X-served-By ${hostname};",
  after  => 'server_name_;',
}

# run and enable nginx Service
service { 'nginx':
  ensure => running,
}

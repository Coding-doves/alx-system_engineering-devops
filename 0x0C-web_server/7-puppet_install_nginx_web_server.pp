# puppet manifest to install nginx
package { 'ngnix':
  ensure => 'installed',
}

file { '/var/www/html/inde.html':
  content => 'Hello World!',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-avaliable/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}

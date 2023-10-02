# creating a custom HTTP header response
# installing nginx
package { 'nginx':
  ensure => installed,
}

# creating a ninx confiuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  notify  => Service['nginx'],
}

# run and enable nginx Service
service { 'nginx':
  ensure   => running,
  enable   => true,
  require  => Package['nginx']
}

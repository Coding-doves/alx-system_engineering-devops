# Replace the line containing "ULIMIT -n 15" with "ULIMIT-*-N 2015"
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 4069\"\n",
}

# Notify Nginx service restart when the file changes
exec { 'restart_nginx':
  command     => '/usr/bin/sudo service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/default/nginx'],
}

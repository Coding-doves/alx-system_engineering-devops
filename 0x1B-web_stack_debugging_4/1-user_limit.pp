# Change OS configuration so it is possible to login with the holberton user
exec { 'change_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}
exec { 'change_to_40':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}

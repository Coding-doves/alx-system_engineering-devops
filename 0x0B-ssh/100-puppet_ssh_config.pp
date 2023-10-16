#!/usr/bin/puppet
# configures ssh with puppet


exec { 'echo':
  path     => ['/bin', '/usr/bin'],
  command  => 'echo "	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns  => [0, 1],
}

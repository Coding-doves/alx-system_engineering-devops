# create a manifest that kills a process named killmenow
exec { 'kill_killmenow':
  command     => 'pkill -f "killmenow"',
  path        => '/usr/bin:/bin',  # Specify the appropriate path to pkill
  onlyif      => 'pgrep -f "killmenow"',
  refreshonly => true,
  logoutput   => true,
}

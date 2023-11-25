#Using Puppet we create a manifest that kills a process named killmenow
exec {'pkill killmenow':
  command     => 'usr/bin/pkill -9 killmenow',
  refreshonly => true,
}

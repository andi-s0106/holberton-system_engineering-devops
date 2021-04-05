#  kills a process named killmenow
exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}

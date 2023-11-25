# Install Flask 2.1.0
exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  creates => '/usr/local/bin/flask',
  require => Package['python3-pip'],
}

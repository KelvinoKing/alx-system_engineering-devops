# Install flask

package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed;
}

exec { 'upgrade_pip':
  command => '/usr/bin/pip3 install --upgrade pip',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

exec { 'install_or_upgrade_flask':
  command => '/usr/bin/pip3 install --upgrade Flask==2.1.0',
  path    => ['/usr/bin'],
  require => Exec['upgrade_pip'],
}

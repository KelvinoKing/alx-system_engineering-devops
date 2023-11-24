# Install flask

package { 'python3-pip':
ensure => installed,
}


package { 'Flask':
  ensure  => '2.1.0',
  require => Package['python3-pip'],
}

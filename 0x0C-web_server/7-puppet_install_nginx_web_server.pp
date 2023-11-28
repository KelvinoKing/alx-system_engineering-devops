# File: nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available':
  ensure => directory,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => 'server {
    listen 80;
    rewrite ^/redirect_me https://kelvino.com permanent;
  }',
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80;',
  line   => 'rewrite ^/redirect_me https://kelvino.com permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

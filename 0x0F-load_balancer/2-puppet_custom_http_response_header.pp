# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create HTML directory and files
file { '/var/www/html':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  content => 'Ceci n\'est pas une page',
}

# Configure Nginx default site
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $::{hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://kelvino.com/;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}",
  require => Package['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

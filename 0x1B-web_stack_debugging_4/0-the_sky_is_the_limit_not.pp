#testing how well web server setup featuring Nginx is doing under pressure

exec { 'config':
  command  => "/bin/sed -i \'s/ULIMIT=\".*\"/ULIMIT=\"-n 1500000\"/\' /\
etc/nginx/nginx.conf",
}
exec { 'restarting':
  command => '/usr/sbin/service nginx restart',
  onlyif  => '/usr/sbin/service nginx reload',
}

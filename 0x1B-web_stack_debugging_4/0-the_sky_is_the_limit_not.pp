#testing how well web server setup featuring Nginx is doing under pressure

exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' \
/etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}

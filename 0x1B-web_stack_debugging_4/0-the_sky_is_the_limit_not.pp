#testing how well web server setup featuring Nginx is doing under pressure

exec { 'fix_error':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx; ; sudo service nginx restart",
}

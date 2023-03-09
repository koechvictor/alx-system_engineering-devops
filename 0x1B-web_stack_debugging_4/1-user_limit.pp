#fix os error change config

exec { 'config':
  command  => "/bin/sed -i \'s/holberton/#holberton/\' /\
etc/security/limits.conf",
}

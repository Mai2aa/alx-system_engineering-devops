# creating a file that contain I love puppet
file { '/tmp/school':
  ensure  => file,
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}


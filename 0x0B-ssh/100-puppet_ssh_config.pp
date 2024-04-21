#!/usr/bin/env bash
#client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# Managed by Puppet\n\n
               Host *\n
               IdentityFile ~/.ssh/school\n
               PasswordAuthentication no\n",
}

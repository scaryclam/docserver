# Deals with any file operations

/home/vagrant/.bashrc:
  file:
    - managed
    - source: salt://bashrc
    - user: vagrant
    - group: vagrant

/etc/supervisor/conf.d/vagrant.conf:
  file.symlink:
    - target: /var/www/docserver/deploy/supervisord/vagrant.conf

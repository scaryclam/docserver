docserver_env:
  file.directory:
    - name: /var/www/docserver_env
    - user: vagrant
    - group: vagrant
    - recurse:
      - user
      - group
      - mode

/var/www/docserver_env:
  virtualenv.managed:
    - use_wheel : False
    - system_site_packages: False
    - requirements: salt:///var/www/docserver/deploy/requirements.txt
    - user: vagrant

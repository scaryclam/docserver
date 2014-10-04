core:
  pkg.installed:
    - pkgs:
      - nginx
      - python-pip
      - python-virtualenv
      - python-dev
      - vim
      - postgresql
      - libxml2-dev
      - libxslt1-dev
      - memcached
      - supervisor
      - gettext
    - refresh: True

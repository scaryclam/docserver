template1_remove:
  cmd.script:
    - user: postgres
    - name: salt://remove_template.sh
    - shell: /bin/bash

template1_create:
  postgres_database:
    - present
    - name: template1
    - encoding: UTF8
    - lc_collate: en_GB.UTF8
    - lc_ctype: en_GB.UTF8
    - template: template0
    - runas: postgres

docserver_user:
  postgres_user.present:
    - name: docserver
    - password: vagrant
    - createdb: true
    - runas: postgres
    - superuser: true

docserver_vagrant:
  postgres_database:
    - present
    - name: docserver_vagrant
    - encoding: UTF8
    - lc_collate: en_GB.UTF8
    - lc_ctype: en_GB.UTF8
    - template: template1
    - runas: postgres


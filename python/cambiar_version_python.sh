# cambiar python por defecto
update-alternatives --install /usr/bin/python python /usr/bin/python2.4 10
update-alternatives --install /usr/bin/python python /usr/bin/python2.5 20

update-alternatives --config python

# Josean7link.org _Personal Server Configuration._

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Linux_Mint_logo_without_wordmark.svg/240px-Linux_Mint_logo_without_wordmark.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Linux_Mint_logo_without_wordmark.svg/240px-Linux_Mint_logo_without_wordmark.svg.png)
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/240px-Python-logo-notext.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/240px-Python-logo-notext.svg.png)

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/MariaDB_colour_logo.svg/320px-MariaDB_colour_logo.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/MariaDB_colour_logo.svg/320px-MariaDB_colour_logo.svg.png)
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Conda_logo.svg/320px-Conda_logo.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Conda_logo.svg/320px-Conda_logo.svg.png)

## _Nginx Configurations Files_
[![N|Solid](http://nginx.org/nginx.png)](https://www.nginx.com/)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/josean7link/Nignx)

### [_phpMyAdmin_]

   [_phpmyadmin_]: <https://www.phpmyadmin.net/>

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/PhpMyAdmin_logo_2010_hidef.svg/320px-PhpMyAdmin_logo_2010_hidef.svg.png)](https://www.phpmyadmin.net/)

#### Rute Config File.
```sh
/etc/nginx/sites-enabled/database.josean7link.org
```

#### Files to Install LEMP Server Linux Nginx Mariadb PHP.
```sh
sudo aptitude install nginx default-libmysqlclient-dev build-essential libldap2-dev mariadb-server-10.3 mariadb-client-10.3 php7.4 php7.4-bz2 php7.4-cli php7.4-common php7.4-curl php7.4-fpm php7.4-gd php7.4-json php7.4-mbstring php7.4-mysql php7.4-opcache php7.4-readline php7.4-xml php7.4-zip python3-dev python3-pip
```

### [_JupyterHub Server Configuration_]

   [_JupyterHub Server Configuration_]: <https://jupyter.org/hub>

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/207px-Jupyter_logo.svg.png)](https://jupyter.org/hub)
#### Rute Config File.

```sh
jamartinez@josean7link:/opt/jupyterhub/etc$ tree | tail
├── jupyterhub
│    └── jupyterhub_config.py
├── nginx
│    └── sites-available
│        └── jupyterhub.josean7link.org
└── systemd
    └── jupyterhub.service
```

#### Documentations to Install Jupyterhub.
```sh
https://github.com/jupyterhub/jupyterhub-the-hard-way/blob/HEAD/docs/installation-guide-hard.md
```

#### Commands to config Jupyterhub, edit each file indicated in the previous guide.
```sh
echo "Comando para crear carpeta /opt/jupyterhub";cd /opt/;sudo ln -s ~/anaconda3/envs/jupyterhub/ jupyterhub
echo "Comando para crear carpeta etc/jupyterhub";cd /opt/jupyterhub;sudo mkdir -p /opt/jupyterhub/etc/jupyterhub
echo "Comando para crear config file";cd /opt/jupyterhub/etc/jupyterhub;sudo /opt/jupyterhub/bin/jupyterhub --generate-config
echo "Comando para crear carpeta nginx y sites-available";sudo mkdir -p /opt/jupyterhub/etc/nginx/sites-available
echo "Comando para crear carpeta systemd/system";sudo mkdir -p /opt/jupyterhub/etc/systemd/system
```

#### Commands to Run Jupyterhub and Stop it.
```sh
echo "Comando para activar el Servidor Jupyterhub"; conda activate jupyterhub; /opt/google/chrome/google-chrome --new-window 'http://jupyterhub.josean7link.org/'; jupyterhub &
```

```sh
echo "Comando para Parar los procesos del Servidor Jupyterhug"; sudo pkill jupyterhub
```

### [Django] & [Rest Framework Apps]

   [Django]: <https://https://docs.djangoproject.com/en/3.2//>
   [Rest Framework Apps]: <https://https://www.django-rest-framework.org/>

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/320px-Django_logo.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/320px-Django_logo.svg.png)
[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Gunicorn_logo_2010.svg/320px-Gunicorn_logo_2010.svg.png)](https://docs.gunicorn.org/en/stable/index.html)

#### The quickstart guide.
```sh
https://docs.djangoproject.com/en/3.2/intro/
https://www.django-rest-framework.org/tutorial/quickstart/
```

#### The _MariaDB_ database software is now installed, but its configuration is not yet complete.
```sh
sudo mariadb -u root -p
CREATE DATABASE ${database};
CREATE USER '${username}'@'localhost' IDENTIFIED BY '${password}';
GRANT ALL PRIVILEGES ON ${database}.* TO '${username}'@'localhost';
FLUSH PRIVILEGES;
exit
```
> _Note_: Be sure to swap out `$database`, `$username` and `$password` with the actual values of your configuration.

#### Gunicorn systemd Service File.
```sh
(venv)jamartinez@josean7link:/${BASE-DIR}/etc$ tree
└── systemd
    └── system
        ├── gunicorn.service
        └── gunicorn.socket
```
- unicorn.socket file.
```sh
[Unit]
Description=$Project gunicorn socket

[Socket]
ListenStream=/run/$Project-gunicorn.sock

[Install]
WantedBy=sockets.target
```
- unicorn.service file.
```sh
[Unit]
Description=$Project gunicorn daemon
Requires=$Project-gunicorn.socket
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/${BASE-DIR}
ExecStart=${BASE-DIR}/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/$Project-gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```
> _Note_: Be sure to swap out `$BASE-DIR` and `$Project` with the actual values of your configuration.

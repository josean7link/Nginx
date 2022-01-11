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
sudo aptitude install nginx default-libmysqlclient-dev build-essential libldap2-dev mariadb-server-10.3 mariadb-client-10.3 php7.4 php7.4-bz2 php7.4-cli php7.4-common php7.4-curl php7.4-fpm php7.4-gd php7.4-json php7.4-mbstring php7.4-mysql php7.4-opcache php7.4-readline php7.4-xml php7.4-zip
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

#### Commands to Run Jupyterhub and Stop it.
```sh
echo "Comando para activar el Servidor Jupyterhub"; conda activate jupyterhub; /opt/google/chrome/google-chrome --new-window 'http://jupyterhub.josean7link.org/'; jupyterhub &
```

```sh
echo "Comando para Parar los procesos del Servidor Jupyterhug"; sudo pkill jupyterhub
```

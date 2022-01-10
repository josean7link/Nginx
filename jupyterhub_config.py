# Configuration file for jupyterhub.

## The public facing URL of the whole JupyterHub application.
#
#          This is the address on which the proxy will bind.
#          Sets protocol, ip, base_url
#  Default: 'http://:8000'
c.JupyterHub.bind_url = 'http://:8000'

## The URL the single-user server should start in.
#
#  `{username}` will be expanded to the user's username
#
#  Example uses:
#
#  - You can set `notebook_dir` to `/` and `default_url` to `/tree/home/{username}` to allow people to
#    navigate the whole filesystem from their notebook server, but still start in their home directory.
#  - Start with `/notebooks` instead of `/tree` if `default_url` points to a notebook instead of a directory.
#  - You can set this to `/lab` to have JupyterLab start by default, rather than Jupyter Notebook.
#  Default: ''
c.Spawner.default_url = '/lab'

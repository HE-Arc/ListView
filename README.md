# ListView
Checklist - Kanban

Back end : Django with Django REST Framework

Front end : VueJS with NUXTJS

# Installation
## Download source
```sh
git clone https://github.com/HE-Arc/ListView.git
```

## Install back end
```sh
cd backend
virtualenv ListView
pip install -r requirements.txt
```

### Local
```sh
echo "debug=True" > .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:8000
```

### Prodction
You need a fonctional postgres server and change the database settings in `backend/settings.py`.

```
python manage.py makemigrations
python manage.py migrate
```

Then you need to configure Nginx and Uwsgi, [installation in french](https://github.com/HE-Arc/ListView/wiki/config_serveur).

## Install front end
```
cd ../ListView_frontend
npm install
```

### Local
```
npm run dev
```

### Production
```
nuxt build
```

Then you need to configure a service to run always NUXTjs. With sv it look like that in `/etc/service/nuxtjs/run`:

```
#!/bin/sh
set -xe
cd /home/poweruser/www/ListView/current/ListView_frontend
exec 2>&1
exec chpst -uwww-data nuxt start
```

Then make it executable and run it

```sh
sudo chmod a+x /etc/service/nuxtjs/run
sudo sv start nuxtjs
```

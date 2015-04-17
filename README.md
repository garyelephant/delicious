## Installation
```
#  get source code
git clone https://github.com/GeiliCode/delicious.git

easy_install virtualenv

virtualenv -p python2.7 --clear delicious_env

source delicious_env/bin/activate

easy_install Django==1.8

cd delicious

# run server
# bind to any address
# python manage.py runserver 0.0.0.0:8000
# bind to localhost
python manage.py runserver

```

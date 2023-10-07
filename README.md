## Installation

### Setup Database

```bash
 sudo su - postgres
 psql
 CREATE DATABASE <analytics>;
 CREATE USER <my-user-name> WITH PASSWORD 'password';
 GRANT ALL PRIVILEGES ON DATABASE <analytics> TO <my-user-name>;
 \q
```

### Setup Backend

```bash
 sudo apt install python3.9-dev
```

* Setting up the virtualenv

```bash
 # create virtualenv
 cd backend/
 virtualenv -p python3.9 venv
 source venv/bin/activate

# install requirements
 pip install -r requirements.txt

cp .secretsenv.sample .secretsenv

* After setting up above things, change the `.secretsenv` file according to your requirements
````

### Running backend for the first time

```bash
 python manage.py migrate
 python manage.py runserver
```


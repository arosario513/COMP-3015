# Final Work

## Installing

Create a new folder and run these commands inside:

```bash
git init
git remote add origin https://github.com/arosario513/COMP-3015.git
git sparse-checkout init
git sparse-checkout add work/final
git pull origin master
```

Inside `work/final` should be this project

## Running with Docker

### Setting up .env

- cd into `final/` and create `.env`
- This will include the password for MariaDB and the secret key for Flask

For the secret key I run a python one-liner, and use that

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

The output will look something like this:

```bash
# Example Output
a131c4973da9e49bbcfb4277a1ca6293849312b12b256c284b63505f08116a0a
```

I'll use that for the `.env` file

```bash
# Example for .env
MARIADB_ROOT_PASSWORD=example123
SECRET_KEY=a131c4973da9e49bbcfb4277a1ca6293849312b12b256c284b63505f08116a0a
```

This file is important, because docker and `main.py` will look for those values

`final/` should look like this:

```bash
# Tree of final/
.
├── app/
├── docker-compose.yaml
├── .env
└── scripts/
```

### Actually running it

First the python image needs to be built

```bash
docker-compose build
```

Now, the docker-compose can be ran

```
docker-compose up -d
```

You can verify it's running properly with `docker-compose ps`

```bash
NAME      IMAGE       COMMAND                  SERVICE   CREATED         STATUS         PORTS
flask     final-web   "flask run --host=0.…"   web       3 seconds ago   Up 2 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp
mariadb   mariadb     "docker-entrypoint.s…"   db        3 seconds ago   Up 2 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp

```

- The website is running at `http://127.0.0.1:5000`
- Now, you should be able to create a user and login

## No Docker
- Alternatively, you can just create a virtual environment inside of `app/` and install the modules needed with  
`pip install -r requirements.txt` and then run `python main.py`.
- If you already have a mysql/mariadb server running, you can use the `init.sql` script to create the tables. Remember to change the host in `main.py` if you do

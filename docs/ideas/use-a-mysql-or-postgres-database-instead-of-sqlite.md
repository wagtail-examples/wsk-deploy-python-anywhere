# Use a mysql or postgres database instead of sqlite

By default, the project uses sqlite3. The developers at `PythonAnywhere` recommend using [MySQL or Postgres for a production database](https://help.pythonanywhere.com/pages/KindsOfDatabases/).

If you'd like to use MySQL for your database, you can deploy MySQL on `PythonAnywhere` and simpy add the database settings to your .env file. **(MySQL is a free service on `PythonAnywhere`).**

If you'd like to use Postgres, you can deploy a Postgres database on `PythonAnywhere` and add the database settings to your .env file. **(Postgres is a paid service on `PythonAnywhere`).**

## MySQL

Create a MySQL database on `PythonAnywhere` from the Dashboard `Databases` tab. There may be a default database already created for you. You can use that database or create a new one.

If you are using the default database, you will need to set a password for the database. Go to the `Databases` tab and in the `MySQL password:` section, add a password and click the `Set MySQL password` button.

### Add these database settings to your .env file.

Go to the root of your project and open  the .env file created earlier. Add the following settings:

```bash
MYSQL_DATABASE='database-name'
MYSQL_USER='Username'
MYSQL_PASSWORD='password'
MYSQL_HOST='Database host address'
MYSQL_PORT=3306
```
You can find your database settings on the `Databases` tab in the `MySQL` section.

The `password` is the password you used to create the database or you just set above.

Save the file.

### Enable the environment variables in the console.

Sqlite doesn't require any additional configuration to run. However, MySQL and Postgres require environment variables to be set to be able to connect to the database.

We configured the wsgi file to load the environment variables from the .env file ealier on in the setup. However, the environment variables are not loaded when you run console commands and they are needed to run the Django commands. You will need to enable them. This is done by updating the `postactivate` file in the virtual environment. You only need to do this once.

From the `Files` tab in the Dashboard, navigate to the virtual environment directory. The directory will be named something like `/home/username/.virtualenvs/your-virtual-environment-name`.

Then navigate to the `bin` directory and open the `postactivate` file and add the following lines:

```bash
set -a; source ~/your-web-app-name/.env; set +a
```

*Here you need to add the path to your .env file. It can be an aboluste path or a relative path. The path should be the same as the path to the .env file in the root of your project. `~/` referes to your account home directory*


## Postgres

The process for setting up a Postgres database is similar to the MySQL process above.

The .env file settings will be different. You can find the settings on the `Databases` tab in the `Postgres` section.

Update your .env file with the following settings:

```bash
POSTGRES_DB='database-name'
POSTGRES_USER='Username'
POSTGRES_PASSWORD='password'
POSTGRES_HOST='Database host address'
POSTGRES_PORT=5432
```

# Deploying this project to PythonAnywhere

This is a step-by-step guide to deploying this project on `PythonAnywhere`.

### 1. Create a PythonAnywhere account

- [Open a free account](
    https://eu.pythonanywhere.com/?affiliate_id=00009409
) and follow the instructions in the deployment guide.

*the link above is a referal link and I will benefit financially if you use the link and later use pythonanywhere paid services or you can go to `https://www.pythonanywhere.com/`*

### 2. Set up a new web app

- Go to the `Web` page your Dashboard and click the `Add a new web app` button.
- You can ignore the 'domain name page' for now and just click on the "Next" button. A free account only allows you to use the `username.pythonanywhere.com`, you can add a custom domain later.
- Select the "Manual configuration" option and click "Next".
- Choose the Python version you want to use (the latest version you have available) and click "Next".
- At the "Manual Configuration" page, click next, we'll set this up manually.

After a short while you will see the app has been created.

### 3. Create a new virtual environment

While this isn't strictly necessary, it's a good idea to create a new virtual environment for your project.

- Go to the "Consoles" tab and start a new bash console.
- Run the following command to create a new virtual environment:
  ```bash
  mkvirtualenv venv_name
  ```
  Replace `ven_name` with the name you want to give your virtual environment.
- Run the following command to activate the virtual environment:
  ```bash
  workon venv_name
  ```
- Leter on the projects python dependencies will be installed in this virtual environment.

### 4. Clone the project

Your site needs to be in a Git repository, so you can clone your project from GitHub or GitLab or any other Git repository.

- Go to the "Consoles" tab and start a new bash console.
- cd into the directory where you want to clone the project, your home directory is a good place to start.
- Clone the project by running:
  ```bash
  git clone your-newley-forked-repo-url
  ```
    Replace `your-newley-forked-repo-url` with the URL of your forked repository.
- Activate the virtual environment you created in the previous step:
  ```bash
  workon venv_name
  ```
- Install the project dependencies by running: *(This will take a few minutes to complete)*
  ```bash
  pip install -r requirements.txt
  ```
- Environment variables are stored in a `.env` file. To be able to use these variables, you need to install the `python-dotenv` package by running:
  ```bash
  pip install python-dotenv
  ```
- Run the following command to create the database tables:
  ```bash
  python manage.py migrate
  ```
- Run the following command to create a superuser:
  ```bash
    python manage.py createsuperuser
    ```
- Run the following command to collect the static files:
  ```bash
  python manage.py collectstatic
  ```

### 5. Create static and media directories

- Go to the "Files" tab and click on the directory where you cloned the project.
- Create a new directory called `static` and another called `media`.
    Your project structure should look something like this:
    ```bash
    .git/
    app/
    docs/
    media/ # <-- New directory
    scripts/
    static/	# <-- New directory
    static_src/
    ```
- Go to the "Web" tab again and undr the `Static files:` section, add the following:
    ```text
    URL: /static/
    Directory: /home/username/path-to-your-project/static/
    ```

    Click the "Add" button and add another static file mapping:
    ```text
    URL: /media/
    Directory: /home/username/path-to-your-project/media/
    Click the "Add" button.
    ```
- Still on the "Web" tab, scroll down to the "Virtualenv" section and add the path to your virtual environment:
    ```text
    /home/username/.virtualenvs/venv_name/
    ```
    Replace `venv_name` with the name of your virtual environment name and `username` with your PythonAnywhere username.
- Still on the "Web" tab, scroll down to the "Code" section and update the `Source code` path to the directory where you cloned the project.

### 6. Update the wsgi file provied by PythonAnywhere

- Go to the "Web" tab and click on the link to the WSGI configuration file. This file will open the file in the editor.
- Delete all the content in the file and replace it with the following:
    ```python
    import os
    import sys
    from dotenv import load_dotenv

    # Add the path to your project directory
    # replace 'project_name' with your project name
    # replace 'username' with your PythonAnywhere username
    path = '/home/username/project_name'

    load_dotenv(os.path.join(path, '.env'))

    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings.production'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
- Go to the "Files" tab and create a new file called `.env` in the root of your project directory.
- Add the following to the `.env` file:
    ```text
    DJANGO_ALLOWED_HOSTS=your-pythonanywhere-domain
    DJANGO_SECRET_KEY=a-secret-key
    ```
    Replace `a-secret-key` with a secret key and `your-pythonanywhere-domain` with your PythonAnywhere allocted domain name.
    Later on, you can add more environment variables to this file if required and if you decide to use a custom domain name, you should add it here in the `DJANGO_ALLOWED_HOSTS` variable.

### Test the project

- Go to the "Web" tab and click the green button to reload your web app.
- After a few seconds, the reload should be complete, you can the click on the link at the top of the page to see the live site.

You should now log into the Wagtail admin and update the site hostname to match your PythonAnywhere domain name.
- Go to the admin page by adding `/admin` to the end of your site URL.
- Log in with the superuser credentials you created earlier.
- Go to the `Settings` section and update the `Site` hostname to match your PythonAnywhere domain name, also update the `Site` port number to `443` to enable HTTPS.

# Further development ideas for the project

You should now have a working version of the project deployed on PythonAnywhere capable of handling production traffic. You'll probably wany to use your own domain name and set up HTTPS for the site.

- Adding your own domain name is described in the [PythonAnywhere documentation](https://help.pythonanywhere.com/pages/CustomDomains/). This also covers setting up HTTPS.

Up to this point the site isn't really that useful, it has a very simple home page and doesn't do much else. In the next section, we'll look at some ideas for further development and start to build out the site with more features.

See the [What Next](./what-next.md) document for ideas on how to expand the project's feature set, improve performance, and make it more user-friendly.

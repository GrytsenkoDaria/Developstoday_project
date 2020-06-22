# Developstoday project

[Developstoday_project](https://developstoday-project.herokuapp.com/posts/) is a small and simple MVP where you can take a look on a list of news and comments to a particular post.
Authorized users can also create posts, as well as upvote and comment on them.

## Getting Started

Here are some instructions to get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Firstly you should clone the project from git:
```
git clone git@github.com:GrytsenkoDaria/developstoday_project.git <repodir>
cd <repodir>
```
Inside the created dir you should create a virtual environment using `pyenv`
>For more details concerning pyenv installation have a look on [these](https://github.com/pyenv/pyenv) link.
>To see all pyenv commands: [here](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local)

```
pyenv virtualenv 3.7.6 <env_name>
pyenv local <env_name>
```
Inside your environmet you should install all packages and modules:
```
pip install -r requirements.txt
```
After all modules are installed successfully go to further steps.

### Main settings

Now we need to set up all the setting to the project.

### 1. Setting up the settings.py

Firstly, you should set up all the setting for the project. In the directory `developstoday/settings/` there are two seettings files:
- **local_settings.example**
- **production.py**

If you want to start the project on your local machine, you should just rename the existing `local_settings.example` file to `local_settings.py` and go to setting `.env` file.

On the other hand, if you want to deploy existing project, don't do anything, just left the `local_settings.example` file as it is. For deployment you will need only `production.py`.

### 2. Setting up the .env file

For project to work correctly we need to determine all variables in our settings file (regardless `local_settings.py` or `production.py`).

Inside the project there is a `.env.example` file, which you should copy and remane to `.env`.
In your newly created `.env` file you just need to fiil the fields with <> by your data.
```
DJANGO_SECRET_KEY=<your_secret_key>
DJANGO_ALLOWED_HOSTS=localhost,
DATABASE_URL=psql://<username>:<password>@127.0.0.1:5432/<db_name>
```

### 3. Migrations

As your DB is not created yet and you alredy have all the migrations in your project, you should run these migrations:
```
python manage.py migrate
```

If it successeded you should have a basic database created and can try to lainch the project from your local machine.
> Only if previosly all settings in `local_settings.py` were setted up!

## Deployment

All the needed settings to deploy are already setted up in the projects. These are:

- *requirements.txt*
- *production.py*
- *Procfile*

**To deploy existing projects on Heroku using Github we need to:**
1. Have an account on [Heroku](https://www.heroku.com/)
2. On the [website](https://dashboard.heroku.com/apps) find the button `Create New App` and fill all the fields.
3. On the tab `Resources` find the field `Add-ons` where we need to downdload `Heroku Postgres` as our DB.
4. Go to tab `Settings` and in field `Config Vars` press `Reveal Config Vars`.
   Here we should fill `Config Vars` with our variables in `production.py`:
   ```
   DATABASE_URL ---> URL created by Heroku
   DJANGO_ALLOWED_HOSTS ---> <your_app_name>.herokuapp.com
   DJANGO_SECRET_KEY ---> <your_secret_key> from `production.py`
   ```
5. Choose the tab `Deploy` and there the field `Deployment method`. 
   Here for more convinient way choose `GitHub` and select the repo name.
   > I describe the way I was doing it. Surely, if another person is going to deploy this project it is better to use Heroku CLI.
6. After connecting the GitHub and Heroku you should in the field `Manual deploy` choose the branch to deploy (`master` as for me) and push `Deploy branch`.
7. The next step is to migrate all the migrations in our project.
   On the tab `Settings` right upper corner find button `More` and select `Run console`.
8. In the console run this code:
   ```
   python manage.py migrate
   ```
9. To fiil out our service with data a dump file `mydata.json` was made. To download the data on Heroku open a console (see previous step) and run command:
   ```
   python manage.py loaddata mydata.json
   ```
   > Some errors mey occur on this step as while previous migrations were made, some users may alredy were created, which differs from our DB.
10. To try if everything works go on the link [Developstoday_project](https://developstoday-project.herokuapp.com/posts/) and have a look on a list of posts.

Additionaly:
- As with `Heroku Postgres` you should download `Heroku Scheduler` where there is an option to run a particular script periodicaly.
- After downloading you should push the button `Add Job` and in the field `Run Command` add:
   ```
   python manage.py refresh_upvotes
   ```
   and set the `Schedule` to `Every day at 12:00 PM`

## Postman collection

For more convinient REST requests testing there were created a `Developstoday collection` inside the Postman with list of variables and directories.
As embed link to the collection you can use [this](https://www.getpostman.com/collections/f709a38bba5d63c205d4).
Every element of the collection is documented inside the collection in the `description` field.  

## Built With

* [Black](https://github.com/psf/black) - Python code formatter
* [flake8](https://github.com/PyCQA/flake8) - Toolkit for checking the code base against coding style (PEP8) and programming errors
* [Postman](https://www.postman.com/) - Used to send REST requests directly within Postman
* [Postgres](https://www.postgresql.org/) - Open source object-relational database system
* [Heroku](https://www.heroku.com/) - A cloud platform that lets to build, deliver, monitor and scale apps
* [Visual Studio Code](https://code.visualstudio.com/) - Source code editor



> All of the deployment settings and deployment as it is, were done for the first time. Some bugs and error may occur by following all the way in this `README.doc` file, for what I beg you a pardon!


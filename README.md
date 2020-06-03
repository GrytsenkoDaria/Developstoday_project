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

```
pyenv virtualenv <env_name>
pyenv local <env_name>
```
Inside your environmet you should install all packages and modules:
```
pip install -r requirements.txt
```
After all modules are installed successfully go to further steps.

### Main settings

Now we need to to set up all the setting to the project.

### 1. Setting up the settings.py

Firstly, you should set up all the setting for the project. In the directory `developstoday/settings/` there is two seettings files:
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

As your DB is not created yet and you alredy have all the migrations on your project, you should run these migrations:
```
python manage.py migrate
```

If it successeded you should have a basic database created and can try to lainch the project from your local machine.
> Only if previosly all settings in `local_settings.py` were setted up!

## Deployment

All the needed settings to deploy are already setted up in the projects. These are:

- requirements.txt
- production.py
- Procfile

**To deploy existing projects on Heroku using Github we need to:**
1. Have an account on [Heroku](https://www.heroku.com/)
2. On the [website](https://dashboard.heroku.com/apps) find the button Create New App and fill all the fields.
3. After creating the App choose the tab `Deploy` and there the field `Deployment method`. 
   Here for more convinient way choose `GitHub` and choose the repo name.
> I describe the way I was doing it. Surely, if another person is going to deploy this project it is better to use Heroku CLI.
4. After connecting the GitHub and Heroku you shoul in the field `Manual deploy` choose the branch to deploy (`master` as for me) and push `Deploy branch`.
5. 

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

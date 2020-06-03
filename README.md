# Developstoday project

[Developstoday_project](https://developstoday-project.herokuapp.com/) is a small and simple MVP where you can take a look on a list of news and comments to a particular post.
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
>For more details concerning pyenv installation have a look on these [link](https://github.com/pyenv/pyenv).

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
- local_settings.example
- production.py

If you want to start the project on your local machine, you should just rename the existing `local_settings.example` file to `local_settings.py` and go to setting `.env` file.

On the other hand, if you want to deploy existing project, don't do anything, just left the `local_settings.example` file as it is. For deployment you will need only `production.py`.

### 2. Setting up the .env file

For project to work correctly we need to determine all variables in our settings file (regardless `local_settings.py` or `production.py`).

Inside the project there is a `.env.example` file, which you shoul copy and remane to `.env`.
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
> If previosly all settings in `local_settings.py` were setted up

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

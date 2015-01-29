{{ cookiecutter.project_name }}
==============================
{{ cookiecutter.project_description }}

# Usage

The following sections contains a short introduction on how to bootstrap and use this project. For more information, please see the documentations of the individual libraries being used.

## Prerequisites

In order to make use of this setup, there are a couple of things that you must already have installed. I won't go into detail with each one, so have a look at the individual documentations.

**1. Install homebrew**

First off, you probably want to install [homebrew](http://) which will make everything so much easier. If you already have macports or fink installed, get rid of it. Homebrew is better.

**2. Make sure your `PATH` is sane**

View your current `PATH` by executing `echo $PATH` in the terminal. You want to make sure that `/usr/local/bin` comes before `/usr/bin`. I use this path, and it seems to be working well: `/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin`

**3. Virtual Machine**:

 - [Vagrant](http://vagrantup.com) - Get the latest version
 - [VirtualBox](https://www.virtualbox.org/) or [Parallels](http://www.parallels.com/) - Whichever you prefer. VirtualBox is free, Parallels is better. (Parellels isn't supported yet.)

**4. Python**:

 - [python 2.7.x](http://python.org) - Get the latest version of python 2, preferably by running `brew install python`. Please do not use the Apple provided python, as it's slightly outdated, and there's no way of knowing what they've done to the poor thing before including it.
 - [pip](https://pip.pypa.io/en/latest/) - You should get a relatively up-to-date one with your python install. Make sure it's up to date with `pip install --upgrade pip`
 - [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) - Install with `pip install virtualenv virtualenvwrapper` and follow the [installation guide for virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

**5. Optional**:

 - [PostgreSQL](http://www.postgresql.org/) - If you choose to run the project on your local machine and only use the virtual machine for "services" (recommended), you will need to install postgresql so you can build the python psycopg2 drivers. Install with `brew install postgresql`

**6. Bonus!**

For fast installs of python dependencies, add the following environment variables to your startup files (.profile or .bash_profile or whatever you're using):
```bash
export PIP_DOWNLOAD_CACHE="$HOME/.pip/cache"
export PIP_FIND_LINKS="$HOME/.pip/wheels"
export PIP_WHEEL_DIR="$HOME/.pip/wheels"
```

And then create the directories:
```bash
mkdir -p $PIP_DOWNLOAD_CACHE $PIP_WHEEL_DIR
```

Also, in `~/.virtualenvs/postmkvirtualenv` add the following:
```bash
pip install wheel
```

Now, every once in a while you're going to want to run `pip wheel -r <requirements file>` in various projects, which will both cache the downloads as well as pre-build a bunch of wheels for you. Then, next time you run `pip install -r <requirements file>` it will be much faster because the files are already built (i.e. no waiting for lxml or pycrypto to compile).


## Bootstrapping

After installing and setting up the prerequisites it should be possible to bootstrap the project in a few simple commmands (executed from the root of the project):

**1. Create virtualenv**
```
mkvirtualenv {{ cookiecutter.repo_name }}
```

**2. Install requirements**

Install the local requirements. This gives you all of the requirements needed for running the project, as well as some handy tools for local development:
```
pip install -r requirements/local.txt
```

**3. Create .env file**

Since a lot of the configuration is done using environment variables, you will need to have these set. This project assumes you'll be using honcho with an .env file (more about this later). Create a basic env file by copying the example:
```
cp src/.env.example src/.env
```

**4. Bootstrap**

Run the bootstrap target in the makefile:
```
make bootstrap
```
This will:
 - Create and provision a new vagrant box with the necessary software (Postgres, Redis and whatever else is needed)
 - Run syncdb
 - Run migrate
 - Load an initial fixture set
 - Create an admin user with username `admin` and password `admin`

## Developing

You're now ready to start developing. While doing so, you'll be using [honcho](https://github.com/nickstenning/honcho) extensively. Please have a look at the [honcho documentation](https://honcho.readthedocs.org/en/latest/) and get familiar with it. In short, it's a process runner that can set environment variables and start multiple processes, interleaving and color coding their output to the console.

While developing, you'll be spending your time in the `src` dir. This is where all of the code should live, and where you'll be running the server and management commands from.

**Starting the development server**

To run the development server, as well as the celery worker, just cd to the `src` directory and run:
```
honcho start
```
This will read the processes in the `Procfile` and start them. The output from each process will be color coded. To stop the development server, press `ctrl+c`. The webserver will be serving on `8010` and Django code reloading will work as usual.

**Running manage.py commands**

To run a manage.py command, execute the following command:
```
honcho run python manage.py <command>
```
This will ensure that environment variables are set up properly when the command is executed.

**Useful aliases**

These commands can be quite a lot of typing. To make it easier, here are some aliases that will speed things up (put them somewhere in your .profile or .bash_profile):
```bash
alias hr="honcho run"
alias hs="honcho start"
alias hm="honcho run python manage.py"
```

Once these are set up, you can run Django management commands by writing only `hm <command>` (i.e. `hm syncdb`, `hm shell` etc.)


## Testing

The makefile at the root of the project contains a couple of tasks for testing:

- `make lint`: runs [flake8](https://pypi.python.org/pypi/flake8) and [pep8-naming]() on the project, reporting any violations of [PEP8](http://legacy.python.org/dev/peps/pep-0008/), as well as some general code issues (unused imports etc.)
- `make test`: runs the test suite.
- `make coverage`: runs the test suite under [coverage](https://pypi.python.org/pypi/coverage) and builds the html output. The output will be in `src/htmlcov/`. This will allow you to see line by line what is being tested and what is not.


## Documentation

TBW


# Principles

## Easy setup

It should be possible to bootstrap the project from a clean checkout to a working project with sample data at any given time using only a couple of commands. This will allow fast re-builds of the project for existing developers, as well as easy on-boarding of new developers. It will also keep the requirements and settings files well-groomed, which will be nice come deploy time.

## Directory layout

 - `bin/` - Shell scripts or other binaries, which arent fit for django management commands.
 - `docs/` - Sphinx project for writing and building documentation
 - `project/` - Various project-related files (documents, mockups, example data, etc.)
 - `requirements/` - Requirements files, one per environemnt (see below)
 - `sandbox/` - Directory in .gitignore which can be used as your local "play-area"
 - `src/` - Actual django project source code

## Environments

The project contains 3 environments. For each environment there is a requirements file, as well as a settings file. The requirements files and the settings files inherit from the base environment.

 - `base` - This is the default environment, and it should be applicable for production, qa, staging, etc. Basically any deployment.
 - `local` - This is the development environment. It should only be used on your local machine (hence the name). It turns on `debug` and adds `django-debug-toolbar`
 - `test` - Environment for testing, if necessary.

It shouldn't be necessary to have any more environments than these. It is imperative that the `local` and `test` environments are kept as close as possible to the `base` environment. This will allow developers to run a version of the project which is very close to what is (or will be) running in production.

## Requirements files

The `base` requirements are ALWAYS pinned to a specific version. This is what is running in production, and hence, what the developers should be running locally as well.

Other requirements need not be pinned down.

## Configuration

All configuration which could change between different deployments, or which is sensitive in nature, is done in environment variables. During development, these variables are loaded with [honcho](https://github.com/nickstenning/honcho) using `.env` files. This has the added benefit of letting you start multiple processes with one command using a procfile (e.g. django development server alongside celery).

All developers work from the same settings file, only changing the environment variables.

## Logging

All logging is sent to standard output or standard error. During development, this means that it will show up in the console. In production, the runtime environment should handle redirecting this in the proper way (be it local files, syslog, a hosted service like splunk or papertrail, or any combination of the above).

## Static assets and media

TBW

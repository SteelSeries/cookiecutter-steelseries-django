# Cookiecutter template for django projects

Template for setting up new django projects using [cookiecutter](http://example.com),
inspired by [Two Scoops of Django](http://twoscoopspress.org/collections/everything/products/two-scoops-of-django-1-6) and [The Twelve-Factor App](http://12factor.net/). Since some aspects of The Twelve-Factor App lies outside the repository (config management, logging, etc.), this template should go hand in hand with deployment and release management taking those things into account.

**Features:**
 - Top-level folders for sphinx docs, requirements files and various project artifacts
 - Vagrant machine pre-configured with Ubuntu 12.04 for both VirtualBox and Parallels
 - Provisioning for base [PostgreSQL](http://www.postgresql.org/), [Redis](http://redis.io/), [RabbitMQ](https://www.rabbitmq.com/) and [elasticsearch](http://www.elasticsearch.org/) installs
 - A battle-hardened .gitignore
 - Standard modern django code layout contained in a subfolder
 - Multiple environments (base, local and test)
 - Makefile for bootstrapping everything, testing, building docs and cleaning up
 - circle.yml file for running tests in [CircleCI](https://circleci.com/)


## Prerequisites

In order to make use of this setup, there are a couple of things that you must already have installed. I won't go into detail with each one, so have a look at the individual documentations.

**1. Install homebrew**

First off, you probably want to install [homebrew](http://) which will make everything so much easier. If you already have macports or fink installed, get rid of it. Homebrew is better.

**2. Make sure your `PATH` is sane**

View your current `PATH` by executing `echo $PATH` in the terminal. You want to make sure that `/usr/local/bin` comes before `/usr/bin`. I use this path, and it seems to be working well: `/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin`

**3. Virtual Machine**:
 - [Vagrant 1.5.x](http://vagrantup.com) - Get the latest version
 - [VirtualBox](http://) or [Parallels](http://) - Whichever you prefer. VirtualBox is free, Parallels is better.

**4. Python**:
 - [python 2.7.x](http://python.org) - Get the latest version of python 2, preferably by running `brew install python`. Please do not use the Apple provided python, as it's slightly outdated, and there's no way of knowing what they've done to the poor thing before including it.
 - [pip](http://) - You should get a relatively up-to-date one with your python install. Make sure it's up to date with `pip install --upgrade pip`
 - [virtualenv](http://) and [virtualenvwrapper](http://) - Install with `pip install virtualenv virtualenvwrapper` and follow the [installation guide for virtualenvwrapper](http://)

**5. Optional**:
 - [Postgresql](http://) - If you choose to run the project on your local machine and only use the virtual machine for "services" (recommended), you will need to install postgresql so you can build the python psycopg2 drivers. Install with `brew install postgresql`

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


## Principles

### Directory layout

 - `bin/` - Shell scripts or other binaries
 - `docs/` - Sphinx project for writing and building documentation
 - `project/` - Various project-related files (documents, mockups, example data, etc.)
 - `requirements/` - Requirements files, one per environemnt (see below)
 - `sandbox/` - Directory in .gitignore which can be used as your local "play-area"
 - `<project name>/` - Actual django project

### Environments

By default, the project contains 3 environments. For each environment there is a requirements file, as well as a settings file. The requirements files and the settings files inherit from the base environment.

 - `base` - This is the default environment, and it should be applicable for production, qa, staging, etc. Basically any deployment.
 - `local` - This is the development environment. It should only be used on your local machine (hence the name). It turns on `debug` and adds `django-debug-toolbar`
 - `test` - Environment for testing, if necessary.

### Configuration



### Tools


**Principles:**
 - If something isn't in source control, it doesn't exist
 - All work is done in a virtualenv, either in the virtual machine or on the local machine
 - All dependencies are declared in requirements.txt files (once a system is live this includes pinning to version numbers)
 - While there are separate environments, the "special" environments should be kept as close to the base environment as possible
 - All configuration that might change between deployments is done in environment variables, even in the dev environment
 - It should be possible to bootstrap an environment with only a couple of commands (mkvirtualenv, pip install, make bootstrap)
 - If there is a best practice way of doing something, it should (probably) be followed

# coding: utf-8
import webbrowser
import os

from fabric.api import task, cd, sudo, env


# Config

env.use_ssh_config = True
env.forward_agent = True
env.abort_on_prompts = True

env.base_dir = '/srv/{{ cookiecutter.repo_name }}'
env.src_dir = os.path.join(env.base_dir, 'src')


# Environments

@task
def dev():
    env.hosts = []


@task
def staging():
    env.hosts = []


@task
def prod():
    env.hosts = []


# Helpers

def git(cmd):
    with cd(env.base_dir):
        return sudo('git %s' % cmd)


def supervisorctl(cmd):
    sudo('supervisorctl %s' % cmd)


def nginx(cmd):
    sudo('/etc/init.d/nginx %s' % cmd)


def kill(pidfile, signal='HUP'):
    sudo('kill -%s `cat %s`' % (signal, pidfile))


def manage(cmd):
    with cd(env.src_dir):
        sudo('envdir env %s/venv/bin/python manage.py %s' % (env.base_dir, cmd))


def collectstatic():
    manage('collectstatic --noinput --clear')


# Tasks

@task
def status():
    sudo('/etc/init.d/nginx status')
    sudo('supervisorctl status')


@task
def compare():
    rev = git('rev-parse HEAD')
    url = "https://github.com/SteelSeries/{{ cookiecutter.repo_name }}/compare/%s...master" % rev
    webbrowser.open_new_tab(url)


@task
def restart():
    pass
    # supervisorctl('restart shop-web:*')
    # supervisorctl('restart shop-queue:*')
    # kill('/run/nginx.pid')


@task
def git_pull():
    git('pull --no-progress')
    git('submodule init')
    git('submodule update')


@task
def deploy():
    git_pull()
    collectstatic()
    restart()


@task
def syncdb():
    manage('syncdb --noinput')
    manage('migrate')

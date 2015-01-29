# Cookiecutter template for django projects

Template for setting up new django projects using [cookiecutter](https://github.com/audreyr/cookiecutter),
inspired by [Two Scoops of Django](http://twoscoopspress.org/collections/everything/products/two-scoops-of-django-1-6) and [The Twelve-Factor App](http://12factor.net/). Since some aspects of The Twelve-Factor App lies outside the repository (config management, logging, etc.), this template should go hand in hand with deployment and release management taking those things into account.

**Features:**
 - Top-level folders for sphinx docs, requirements files and various project artifacts
 - Vagrant machine pre-configured with Ubuntu 12.04 for both VirtualBox and Parallels
 - Provisioning for base [PostgreSQL](http://www.postgresql.org/), [Redis](http://redis.io/), [RabbitMQ](https://www.rabbitmq.com/), [elasticsearch](http://www.elasticsearch.org/) and [Neo4j](http://neo4j.com/) installs
 - A battle-hardened .gitignore
 - Standard modern django code layout contained in a subfolder
 - Multiple environments (base, local and test)
 - Makefile for bootstrapping everything, testing, building docs and cleaning up
 - circle.yml file for running tests in [CircleCI](https://circleci.com/)
 - gulp setup for easy building of assets and minification of images

Note: This setup is thorougly tested on OS X. You might have to adjust appropriately for other platforms.

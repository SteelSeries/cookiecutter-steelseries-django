.PHONY: clean-pyc

help:
	@echo "bootstrap - bootstrap a local dev environment in vagrant"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean - remove various artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests"
	@echo "coverage - check code coverage"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

bootstrap:
	vagrant up
	cd {{ cookiecutter.repo_name }} && \
	honcho run python manage.py syncdb --noinput && \
	honcho run python manage.py migrate && \
	honcho run python -c "from django.db import DEFAULT_DB_ALIAS as db; from django.contrib.auth.models import User; User.objects.db_manager(db).create_superuser('admin', 'admin@example.com', 'admin')"


clean-pyc:
	find . -type d -name "__pycache__" -print0 | xargs -0 rm -rf
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	rm -rf htmlcov/

lint:
	flake8 --max-line-length=100 {{ cookiecutter.repo_name }}

test:
	@echo "Not implemented"

coverage:
	@echo "Not implemented"

docs:
	@echo "Not implemented"

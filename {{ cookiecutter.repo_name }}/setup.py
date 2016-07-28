from setuptools import setup

with open('requirements/base.txt', 'r') as f:
    requires = [l.strip() for l in f if l.strip() and not l.startswith('#')]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='1.0.0',
    license='No.',
    packages=['{{ cookiecutter.repo_name }}'],
    package_dir={
        '{{ cookiecutter.repo_name }}': 'src',
    },
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
)

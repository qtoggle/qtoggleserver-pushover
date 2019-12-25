
from setuptools import setup, find_namespace_packages

from qtoggleserver.pushover import VERSION


setup(
    name='qtoggleserver-pushover',
    version=VERSION,
    description='PushOver notifications for qToggleServer',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),

    install_requires=[
        'aiohttp',
        'jinja2'
    ]
)

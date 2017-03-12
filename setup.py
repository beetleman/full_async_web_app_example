#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'aiodns==1.1.1',
    'aiohttp==1.3.3',
    'aiopg==0.13.0',
    'cchardet==1.1.3',
    'peewee==2.9.0',
    'peewee-async==0.5.7',
    'gunicorn==19.7.0',
    'peewee-migrate==0.11.0'
]

test_requirements = [
    'pytest-aiohttp==0.1.3'
]

setup(
    name='full_async_web_app_example',
    version='0.1.0',
    description="Example",
    long_description=readme + '\n\n' + history,
    author="Mateusz Probachta",
    author_email='mateusz.probachta@pragmaticcoders.com',
    url='https://github.com/beetleman/full_async_web_app_example',
    packages=[
        'full_async_web_app_example',
    ],
    package_dir={'full_async_web_app_example':
                 'full_async_web_app_example'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='full_async_web_app_example',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

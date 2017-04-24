import setuptools

setuptools.setup(
    name="full_async_web_app_example",
    version="0.1.0",
    url="https://github.com/beetleman/full_async_web_app_example",

    author="Mateusz Probachta",
    author_email="mateusz.probachta@gmail.com",

    description="example of python full async app",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
      'aiodns==1.1.1',
      'aiohttp==1.3.3',
      'aiopg==0.13.0',
      'cchardet==1.1.3',
      'peewee==2.9.0',
      'peewee-async==0.5.7',
      'gunicorn==19.7.0',
      'peewee-migrate==0.11.0'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
    ],
)

import os
from setuptools import setup, find_packages
import cmsplugin_googlemap as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="cmsplugin-googlemap",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, cms, plugin, googlemap, maps',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold@bitmazk.com',
    url="https://github.com/bitmazk/cmsplugin-googlemap",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4.3',
        'South',
        'django-cms',
        'Pillow',
    ],
    tests_require=[
        'fabric',
        'factory_boy<2.0.0',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
        'flake8',
        'ipdb',
    ],
    test_suite='cmsplugin_googlemap.tests.runtests.runtests',
)

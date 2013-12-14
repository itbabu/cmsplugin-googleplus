import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cmsplugin-googleplus',
    version='0.3.6',
    include_package_data=True,
    license='MIT License',
    description='Django-CMS plugin for Google Plus Activities',
    long_description=README,
    url='https://github.com/itbabu/cmsplugin-googleplus',
    author='Marco Badan',
    author_email='info@marcobadan.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'google-api-python-client>=1.2',
        'python-dateutil>=2.2'
    ],
    tests_require=[
        'mock>=1.0.1',
        'django-nose>=1.2'
    ],
    packages=find_packages()
)
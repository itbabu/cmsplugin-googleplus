from __future__ import unicode_literals
import os
import sys

from django.conf import settings


def configure():
    if not settings.configured:

        # Helper function to extract absolute path
        location = lambda x: os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'cmsplugin_googleplus', 'tests', 'example_project', x)

        test_settings = {
            'LANGUAGE_CODE': 'en',
            'LANGUAGES': (
                ('en', 'English'),
            ),
            'DATABASES': {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                },
            },
            'INSTALLED_APPS': [
            'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'django.contrib.humanize',
                'south',
                'cms',
                'mptt',
                'menus',
                'sekizai',
                'djangocms_admin_style',
                'django.contrib.admin',
                'cmsplugin_googleplus'],
            'TEMPLATE_CONTEXT_PROCESSORS': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'cms.context_processors.media',
                'sekizai.context_processors.sekizai',
            ),
            'TEMPLATE_DIRS': (
                location('templates'),
            ),
            'ROOT_URLCONF': 'cmsplugin_googleplus.tests.example_project.urls',

            'MIDDLEWARE_CLASSES': (
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.locale.LocaleMiddleware',
                'django.middleware.doc.XViewMiddleware',
                'django.middleware.common.CommonMiddleware',
                'cms.middleware.page.CurrentPageMiddleware',
                'cms.middleware.user.CurrentUserMiddleware',
                'cms.middleware.toolbar.ToolbarMiddleware',
                'cms.middleware.language.LanguageCookieMiddleware',
            ),
            'STATIC_URL': '/static/',
            'ADMINS': ('admin@example.com',),
            'DEBUG': False,
            'SITE_ID': 1,
            'APPEND_SLASH': True,
            'CMS_TEMPLATES': (('nav_playground.html', 'Test Template'),)
        }

        settings.configure(**test_settings)


def run_tests(*test_args):
    from django_nose import NoseTestSuiteRunner
    test_runner = NoseTestSuiteRunner()
    if not test_args:
        test_args = ['cmsplugin_googleplus']
    num_failures = test_runner.run_tests(test_args)
    if num_failures:
        sys.exit(num_failures)


if __name__ == '__main__':
    args = sys.argv[1:]

    if args:
        # Some args specified.  Check to see if any nose options have been
        # specified.  If they have, then don't set any
        has_options = any([x.startswith('--') for x in args])
        if not has_options:
            args.extend(['-s', '-x', '--with-specplugin'])
        else:
            # Remove options as nose will pick these up from sys.argv
            args = [arg for arg in args if not arg.startswith('-')]

    configure()
    run_tests(*args)

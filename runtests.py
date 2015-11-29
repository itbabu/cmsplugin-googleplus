from __future__ import unicode_literals

import os
import sys

import django
from django.conf import settings

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
]


def configure():
    if not settings.configured:

        # Helper function to extract absolute path
        location = lambda x: os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
                'cmsplugin_googleplus', 'tests', 'example_project', x)

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
                'cms',
                'treebeard',
                'menus',
                'sekizai',
                'djangocms_admin_style',
                'django.contrib.admin',
                'cmsplugin_googleplus'],
            'ROOT_URLCONF': 'cmsplugin_googleplus.tests.example_project.urls',

            'MIDDLEWARE_CLASSES': (
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.locale.LocaleMiddleware',
                'django.middleware.common.CommonMiddleware',
                'cms.middleware.user.CurrentUserMiddleware',
                'cms.middleware.page.CurrentPageMiddleware',
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
        if django.VERSION < (1, 8, 0):
            test_settings['TEMPLATE_CONTEXT_PROCESSORS'] = \
                TEMPLATE_CONTEXT_PROCESSORS
            test_settings['TEMPLATE_DIRS'] = [location('templates'), ]
        else:
            test_settings['TEMPLATES'] = [
                {
                    'BACKEND':
                        'django.template.backends.django.DjangoTemplates',
                    'DIRS': [
                        location('templates'),
                    ],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
                        'debug': True
                    },
                },
            ]
        settings.configure(**test_settings)


def run_tests(*test_args):
    if not test_args:
        test_args = ['cmsplugin_googleplus']

    # see:
    # https://docs.djangoproject.com/en/dev/releases/1.7/#standalone-scripts
    django.setup()
    from django.core.management import call_command
    call_command("makemigrations", "cmsplugin_googleplus", database='default')
    call_command("migrate", database='default')

    from django_nose import NoseTestSuiteRunner
    failures = NoseTestSuiteRunner().run_tests(test_args)
    if failures:  # pragma: no cover
        sys.exit(failures)


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

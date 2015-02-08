# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GooglePlusActivities',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('render_template', models.CharField(max_length=100, verbose_name='template', choices=[('cmsplugin_googleplus/twitter_bootstrap.html', 'Example Template using Twitter Bootstrap')])),
                ('items', models.SmallIntegerField(default=5, help_text='Number of Google Plus activities to return. From 1 to 100. Default is 10.', verbose_name='item', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('truncate_chars', models.PositiveIntegerField(default=150, help_text='Truncates the content, annotation and attachment after a certain number of characters.', verbose_name='truncate chars')),
                ('google_user', models.CharField(help_text='The ID of the user to get activities for', max_length=75, verbose_name='Google+ User Id', blank=True)),
                ('query', models.CharField(help_text='Full-text search query string.', max_length=250, verbose_name='search query', blank=True)),
                ('preferred_language', models.CharField(blank=True, help_text='Optional. Specify the preferred language to search with.', max_length=10, verbose_name='preferred language', choices=[('af', 'Afrikaans'), ('am', 'Amharic'), ('ar', 'Arabic'), ('eu', 'Basque'), ('bn', 'Bengali'), ('bg', 'Bulgarian'), ('ca', 'Catalan'), ('zh-HK', 'Chinese (Hong Kong)'), ('zh-CN', 'Chinese (Simplified)'), ('zh-TW', 'Chinese (Traditional)'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en-GB', 'English (UK)'), ('en-US', 'English (US)'), ('et', 'Estonian'), ('fil', 'Filipino'), ('fi', 'Finnish'), ('fr', 'French'), ('fr-CA', 'French (Canadian)'), ('gl', 'Galician'), ('de', 'German'), ('el', 'Greek'), ('gu', 'Gujarati'), ('iw', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('id', 'Indonesian'), ('it', 'Italian'), ('ja', 'Japanese'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lv', 'Latvian'), ('lt', 'Lithuanian'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('no', 'Norwegian'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt-BR', 'Portuguese (Brazil)'), ('pt-PT', 'Portuguese (Portugal)'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sr', 'Serbian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('es', 'Spanish'), ('es-419', 'Spanish (Latin America)'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zu', 'Zulu')])),
                ('order_by', models.CharField(default='recent', help_text="Optional. Specifies how to order search results. 'best': Sort activities by relevance to the user, most relevant first, 'recent': Sort activities by published date, most recent first.", max_length=20, blank=True, choices=[('best', 'best'), ('recent', 'recent')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

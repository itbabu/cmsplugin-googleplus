# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_googleplus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleplusactivities',
            name='google_api_key',
            field=models.CharField(max_length=75, help_text='To use the Google+ API, you must register your project on the Google Developers Console and get a Google API key.', verbose_name='Google API key', default='invalid key'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='googleplusactivities',
            name='order_by',
            field=models.CharField(max_length=20, choices=[('best', 'best'), ('recent', 'recent')], verbose_name='order by', default='recent', blank=True, help_text="Optional. Specifies how to order search results. 'best': Sort activities by relevance to the user, most relevant first, 'recent': Sort activities by published date, most recent first."),
        ),
    ]

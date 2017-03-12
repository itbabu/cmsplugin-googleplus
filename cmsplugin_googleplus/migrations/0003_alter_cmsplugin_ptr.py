# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_googleplus', '0002_add_google_api_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleplusactivities',
            name='cmsplugin_ptr',
            field=models.OneToOneField(
                to='cms.CMSPlugin', auto_created=True, primary_key=True, parent_link=True,
                related_name='cmsplugin_googleplus_googleplusactivities', serialize=False),
        ),
    ]

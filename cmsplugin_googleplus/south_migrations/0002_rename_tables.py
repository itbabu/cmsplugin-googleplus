# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('cmsplugin_googleplusactivities', 'cmsplugin_googleplus_googleplusactivities')


    def backwards(self, orm):
        db.rename_table('cmsplugin_googleplus_googleplusactivities', 'cmsplugin_googleplusactivities')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_googleplus.googleplusactivities': {
            'Meta': {'object_name': 'GooglePlusActivities', 'db_table': "u'cmsplugin_googleplus_googleplusactivities'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'google_user': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'items': ('django.db.models.fields.SmallIntegerField', [], {'default': '5'}),
            'order_by': ('django.db.models.fields.CharField', [], {'default': "'recent'", 'max_length': '20', 'blank': 'True'}),
            'preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'render_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'truncate_chars': ('django.db.models.fields.PositiveIntegerField', [], {'default': '150'})
        }
    }

    complete_apps = ['cmsplugin_googleplus']
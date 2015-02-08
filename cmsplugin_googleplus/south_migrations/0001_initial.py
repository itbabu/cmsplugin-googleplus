# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GooglePlusActivities'
        db.create_table(u'cmsplugin_googleplusactivities', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('render_template', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('items', self.gf('django.db.models.fields.SmallIntegerField')(default=5)),
            ('truncate_chars', self.gf('django.db.models.fields.PositiveIntegerField')(default=150)),
            ('google_user', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('preferred_language', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('order_by', self.gf('django.db.models.fields.CharField')(default='recent', max_length=20, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_googleplus', ['GooglePlusActivities'])


    def backwards(self, orm):
        # Deleting model 'GooglePlusActivities'
        db.delete_table(u'cmsplugin_googleplusactivities')


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
            'Meta': {'object_name': 'GooglePlusActivities', 'db_table': "u'cmsplugin_googleplusactivities'", '_ormbases': ['cms.CMSPlugin']},
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
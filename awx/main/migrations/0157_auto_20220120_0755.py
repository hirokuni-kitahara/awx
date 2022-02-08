# Generated by Django 2.2.20 on 2022-01-20 07:55

import awx.main.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0156_capture_mesh_topology'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='playbook_integrity_result',
            field=awx.main.fields.JSONField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='playbook_integrity_verified',
            field=models.BooleanField(blank=True, default=None, editable=False, help_text='Overall result of playbook integrity verification', null=True),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='playbook_integrity_result',
            field=awx.main.fields.JSONField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='playbook_integrity_verified',
            field=models.BooleanField(blank=True, default=None, editable=False, help_text='Overall result of playbook integrity verification', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='playbook_integrity_enabled',
            field=models.BooleanField(blank=True, default=False, help_text='If enabled, integrity check for a playbook will be done before execution'),
        ),
        migrations.AddField(
            model_name='project',
            name='playbook_integrity_keyless_signer_id',
            field=models.CharField(
                blank=True,
                default='',
                help_text='A signer id string for keyless playbook integrity check',
                max_length=1024,
                verbose_name='signer id string for keyless playbook integrity check',
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='playbook_integrity_latest_result',
            field=awx.main.fields.JSONField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='playbook_integrity_public_key',
            field=awx.main.fields.JSONField(blank=True, default=[], help_text='A list of base64 encoded public keys'),
        ),
        migrations.AddField(
            model_name='project',
            name='playbook_integrity_signature_type',
            field=models.CharField(
                blank=True,
                default='',
                help_text='A signature type for playbook integrity check',
                max_length=1024,
                verbose_name='signature type for playbook integrity check',
            ),
        ),
        migrations.AddField(
            model_name='projectupdate',
            name='playbook_integrity_result',
            field=awx.main.fields.JSONField(blank=True, default=None, editable=False, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 13:38
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0036_auto_20170221_1235'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('sent_to', models.EmailField(max_length=128)),
                ('message', models.TextField()),
                ('contact_type', models.CharField(choices=[('chapter', 'Django Girls Local Organizers'), ('support', 'Django Girls HQ (Support Team)')], default='chapter', max_length=20, verbose_name='Who do you want to contact?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_successfully', models.BooleanField(default=True)),
                ('event', models.ForeignKey(blank=True, help_text='required for contacting a chapter', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Event')),
            ],
            options={
                'ordering': ('-created_at',),
            },
            bases=(models.Model,),
        )
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
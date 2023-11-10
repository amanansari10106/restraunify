# Generated by Django 4.1.7 on 2023-04-18 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_domainsmodel'),
        ('templatesapp', '0003_templatesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwebsites',
            name='domain',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usersapp.domainsmodel'),
        ),
    ]

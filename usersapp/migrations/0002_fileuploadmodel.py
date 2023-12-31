# Generated by Django 4.1.7 on 2023-04-16 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='userUploads/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.cuser')),
            ],
        ),
    ]

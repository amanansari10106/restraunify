# Generated by Django 4.1.7 on 2023-06-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesapp', '0007_templatesmodel_image_templatesmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwebsites',
            name='name',
            field=models.CharField(default='Website Name', max_length=100),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupphotos',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='group_images'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201209_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webgl_project',
            name='thumbnail',
            field=models.ImageField(default='media/thumbnail_default_png', null=True, upload_to='thumbnail'),
        ),
    ]

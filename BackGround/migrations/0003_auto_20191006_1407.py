# Generated by Django 2.2.1 on 2019-10-06 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackGround', '0002_loginuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='description',
            new_name='type_description',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='type_name',
        ),
    ]

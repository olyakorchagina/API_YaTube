# Generated by Django 2.2.16 on 2022-10-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221031_1258'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='users_cannot_follow_themselves',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='users_cannot_follow_themselves'),
        ),
    ]

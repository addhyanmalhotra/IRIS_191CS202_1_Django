# Generated by Django 3.1.2 on 2020-10-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_auto_20201011_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='InStock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactions',
            name='isReturned',
            field=models.BooleanField(default=False),
        ),
    ]

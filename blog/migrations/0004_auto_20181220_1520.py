# Generated by Django 2.0.6 on 2018-12-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_upvotes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

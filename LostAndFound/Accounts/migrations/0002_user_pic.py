# Generated by Django 3.1.1 on 2020-11-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(blank=True, upload_to='pictures/profiels'),
        ),
    ]

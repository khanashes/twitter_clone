# Generated by Django 3.2.3 on 2021-07-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0003_tweet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]

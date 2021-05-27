# Generated by Django 3.2.3 on 2021-05-26 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
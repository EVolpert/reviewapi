# Generated by Django 2.0.6 on 2018-06-26 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_auto_20180626_1641"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviewer",
            name="user",
        ),
        migrations.AlterField(
            model_name="review",
            name="reviewer",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name="Reviewer",
        ),
    ]

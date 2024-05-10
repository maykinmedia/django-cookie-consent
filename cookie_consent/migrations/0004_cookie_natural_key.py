# Generated by Django 4.2.13 on 2024-05-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cookie_consent", "0003_alter_cookiegroup_varname"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="cookie",
            constraint=models.UniqueConstraint(
                fields=("cookiegroup", "name", "domain"), name="natural_key"
            ),
        ),
    ]
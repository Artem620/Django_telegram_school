# Generated by Django 4.2.1 on 2024-10-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_predment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='predment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

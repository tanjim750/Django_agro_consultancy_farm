# Generated by Django 4.1.3 on 2022-11-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0015_testimonia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

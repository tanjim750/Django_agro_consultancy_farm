# Generated by Django 4.1.3 on 2022-11-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0004_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd_img', models.ImageField(upload_to='img')),
                ('bd_title', models.CharField(max_length=100)),
                ('button1N', models.CharField(max_length=100)),
                ('button2N', models.CharField(max_length=100)),
                ('button1L', models.CharField(max_length=100)),
                ('button2L', models.CharField(max_length=100)),
                ('topTx', models.CharField(max_length=100)),
                ('topTi', models.CharField(max_length=100)),
                ('conTi', models.CharField(max_length=100)),
                ('locationT', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('emailT', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('numberT', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('bd_title', models.CharField(max_length=100)),
                ('button1N', models.CharField(max_length=100)),
                ('button2N', models.CharField(max_length=100)),
                ('button1L', models.CharField(max_length=100)),
                ('button2L', models.CharField(max_length=100)),
                ('sr_text', models.CharField(max_length=100)),
                ('sr_title', models.CharField(max_length=100)),
                ('sr_details', models.TextField()),
                ('sr_btn', models.CharField(max_length=100)),
                ('sr_btnL', models.CharField(max_length=100)),
                ('banner1T', models.CharField(max_length=100)),
                ('banner1PD', models.TextField()),
                ('banner2T', models.CharField(max_length=100)),
                ('banner2PD', models.TextField()),
                ('banner3T', models.CharField(max_length=100)),
                ('banner3PD', models.TextField()),
                ('banner4T', models.CharField(max_length=100)),
                ('banner4PD', models.TextField()),
                ('banner5T', models.CharField(max_length=100)),
                ('banner5PD', models.TextField()),
            ],
        ),
    ]
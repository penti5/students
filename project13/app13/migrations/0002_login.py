# Generated by Django 2.2.3 on 2019-08-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app13', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
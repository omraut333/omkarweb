# Generated by Django 3.1.6 on 2021-02-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_home_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_me_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

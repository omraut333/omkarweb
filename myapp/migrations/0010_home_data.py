# Generated by Django 3.1.6 on 2021-02-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_education_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('tag', models.CharField(max_length=120)),
                ('desc', models.TextField()),
            ],
        ),
    ]

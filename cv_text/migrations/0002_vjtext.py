# Generated by Django 2.0.3 on 2018-03-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VJText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vltext', models.TextField()),
            ],
        ),
    ]

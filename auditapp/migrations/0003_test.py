# Generated by Django 2.1.4 on 2018-12-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditapp', '0002_contributor_submittal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly_name', models.CharField(max_length=80, verbose_name='Name')),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraps', '0002_auto_20190724_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='l_name',
            field=models.CharField(default=0, max_length=255, verbose_name='Min of technology'),
            preserve_default=False,
        ),
    ]

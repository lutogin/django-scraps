# Generated by Django 2.2.3 on 2019-08-04 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraps', '0010_auto_20190731_1806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-id'], 'verbose_name': 'Content', 'verbose_name_plural': 'Contents'},
        ),
    ]
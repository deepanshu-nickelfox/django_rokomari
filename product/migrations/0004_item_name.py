# Generated by Django 2.0.3 on 2020-08-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200814_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
    ]
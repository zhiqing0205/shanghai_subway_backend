# Generated by Django 4.2.8 on 2024-03-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0003_alter_itedata_fn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itedata',
            name='cfo',
            field=models.FloatField(blank=True, null=True, verbose_name='cfo'),
        ),
    ]

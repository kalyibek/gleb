# Generated by Django 4.1.1 on 2022-10-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medshows', '0002_type_alter_medicalshows_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalshows',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]

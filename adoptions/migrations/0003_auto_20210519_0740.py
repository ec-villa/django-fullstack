# Generated by Django 3.0 on 2021-05-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_exampledata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampledata',
            name='start_date',
            field=models.DateField(),
        ),
    ]

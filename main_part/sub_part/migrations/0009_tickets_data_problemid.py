# Generated by Django 3.1.7 on 2021-03-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_roles_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets_data',
            name='problemid',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

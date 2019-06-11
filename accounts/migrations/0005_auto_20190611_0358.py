# Generated by Django 2.2.2 on 2019-06-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_college_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='college_name',
            field=models.CharField(choices=[('', 'Select College'), ('nitkkr', 'NIT KURUKSHETRA'), ('thappar', 'THAPPAR , PATIALA')], default='', max_length=20),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Unverified', 'Unverified')], default='Unverified', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

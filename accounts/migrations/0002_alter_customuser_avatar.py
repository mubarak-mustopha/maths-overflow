# Generated by Django 4.0.10 on 2024-07-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', upload_to='profile/'),
        ),
    ]

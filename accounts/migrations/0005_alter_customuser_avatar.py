# Generated by Django 4.0.10 on 2024-07-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='images/profile/avatar_rwpw3x', upload_to='profile/'),
        ),
    ]

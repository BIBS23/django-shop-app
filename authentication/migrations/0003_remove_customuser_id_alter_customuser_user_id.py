# Generated by Django 5.1.4 on 2024-12-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]

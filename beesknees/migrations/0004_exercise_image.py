# Generated by Django 4.2.3 on 2023-07-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beesknees', '0003_rename_exercises_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(default='image of muscle', upload_to='files/muscleimage'),
        ),
    ]
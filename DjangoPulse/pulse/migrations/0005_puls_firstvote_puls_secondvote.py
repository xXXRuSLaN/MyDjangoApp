# Generated by Django 4.2.6 on 2023-11-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0004_pulschoice_puls_fchoice_puls_schoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='puls',
            name='firstVote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='puls',
            name='secondVote',
            field=models.IntegerField(default=0),
        ),
    ]
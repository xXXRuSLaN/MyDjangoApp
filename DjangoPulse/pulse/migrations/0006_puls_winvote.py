# Generated by Django 4.2.6 on 2023-11-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0005_puls_firstvote_puls_secondvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='puls',
            name='winVote',
            field=models.IntegerField(default=0),
        ),
    ]

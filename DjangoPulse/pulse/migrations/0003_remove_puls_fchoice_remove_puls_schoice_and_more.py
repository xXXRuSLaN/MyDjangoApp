# Generated by Django 4.2.6 on 2023-11-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0002_delete_pulsmsgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puls',
            name='fchoice',
        ),
        migrations.RemoveField(
            model_name='puls',
            name='schoice',
        ),
        migrations.DeleteModel(
            name='polsChoice',
        ),
    ]

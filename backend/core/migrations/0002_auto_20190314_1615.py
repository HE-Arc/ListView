# Generated by Django 2.1.7 on 2019-03-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='belongs_to',
            new_name='team_id',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='belongs_to',
            new_name='board_id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='belongs_to',
            new_name='list_id',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='part_of',
            new_name='users_id',
        ),
    ]

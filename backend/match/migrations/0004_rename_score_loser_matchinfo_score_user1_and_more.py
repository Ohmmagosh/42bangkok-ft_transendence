# Generated by Django 5.0.2 on 2024-03-06 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_matchinfo_score_loser_matchinfo_score_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchinfo',
            old_name='score_loser',
            new_name='score_user1',
        ),
        migrations.RenameField(
            model_name='matchinfo',
            old_name='score_winner',
            new_name='score_user2',
        ),
    ]

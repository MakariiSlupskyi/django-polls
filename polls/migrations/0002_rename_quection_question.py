# Generated by Django 5.0.6 on 2024-06-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quection',
            new_name='Question',
        ),
    ]
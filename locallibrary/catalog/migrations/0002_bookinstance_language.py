# Generated by Django 5.0.2 on 2024-04-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='Language',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='en', help_text='Language', max_length=2),
        ),
    ]

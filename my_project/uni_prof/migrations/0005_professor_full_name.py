# Generated by Django 5.1.4 on 2025-01-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_prof', '0004_professor_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='full_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_rating_left_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='overall_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
    ]

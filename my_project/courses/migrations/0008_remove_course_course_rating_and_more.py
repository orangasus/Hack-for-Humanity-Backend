# Generated by Django 5.1.4 on 2025-01-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_course_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_rating',
        ),
        migrations.AddField(
            model_name='course',
            name='avg_cognitive_load_rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='avg_course_rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='avg_delivery_support_rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='avg_engagement_enjoyment_rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='avg_usefulness_relevance_rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='has_reviews',
            field=models.BooleanField(default=False),
        ),
    ]

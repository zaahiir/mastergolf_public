# Generated by Django 5.0.7 on 2025-02-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_alter_coursemodel_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='courseImage',
            field=models.ImageField(blank=True, null=True, upload_to='course_images/'),
        ),
    ]

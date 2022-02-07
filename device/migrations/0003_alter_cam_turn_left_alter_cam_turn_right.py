# Generated by Django 4.0.1 on 2022-02-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_alter_cam_slug_alter_cam_turn_left_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cam',
            name='turn_left',
            field=models.FloatField(blank=True, default=0, help_text='Turn Camera to left'),
        ),
        migrations.AlterField(
            model_name='cam',
            name='turn_right',
            field=models.FloatField(blank=True, default=0, help_text='Turn Camera to Right'),
        ),
    ]

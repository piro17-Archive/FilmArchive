# Generated by Django 4.0.6 on 2022-08-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framesharings', '0004_alter_frame_framelikedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='frameweeklike',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='주간좋아요수'),
        ),
        migrations.AlterField(
            model_name='frame',
            name='framelikedate',
            field=models.TextField(blank=True, null=True, verbose_name='좋아요날짜'),
        ),
    ]
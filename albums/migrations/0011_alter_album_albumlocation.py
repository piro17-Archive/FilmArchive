# Generated by Django 4.0.6 on 2022-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_alter_album_albumlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumlocation',
            field=models.CharField(blank=True, default='126.97063477079135, 37.554357189598775,저장된 장소가 없습니다.', max_length=50, null=True, verbose_name='앨범위치'),
        ),
    ]
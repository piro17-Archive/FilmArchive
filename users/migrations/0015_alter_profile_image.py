from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y%m%d', verbose_name='프로필사진'),
        ),
    ]

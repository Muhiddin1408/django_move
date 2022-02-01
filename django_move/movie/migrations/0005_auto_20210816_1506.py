# Generated by Django 3.1.7 on 2021-08-16 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20210816_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='description',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movie.movie', verbose_name='movie'),
        ),
    ]
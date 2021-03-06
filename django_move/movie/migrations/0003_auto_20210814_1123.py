# Generated by Django 3.2.6 on 2021-08-14 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'star of ruiting',
                'verbose_name_plural': 'star of ruiting',
                'ordering': ['-value'],
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='movie.Actor', verbose_name='Actor va rejissor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='directors', to='movie.Actor', verbose_name='Actor va rejissor'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='movie.review', verbose_name='parent'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ratingstar', verbose_name='star')),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': 'ratings',
            },
        ),
    ]

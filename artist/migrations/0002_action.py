# Generated by Django 3.2.4 on 2021-06-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('dir_name', models.CharField(max_length=50)),
                ('prod_year', models.IntegerField()),
                ('best_movie_actor', models.CharField(max_length=50)),
                ('act_bio', models.TextField()),
                ('actor_fav', models.BooleanField(default=True)),
            ],
        ),
    ]

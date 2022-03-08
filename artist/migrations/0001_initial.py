# Generated by Django 3.2.4 on 2021-06-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horror_genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('dirctor_name', models.CharField(max_length=50)),
                ('production_year', models.IntegerField()),
                ('best_movie_actor', models.CharField(max_length=50)),
                ('actorsbio', models.TextField()),
                ('actorsimage', models.ImageField(default='', null=True, upload_to='actor_image/')),
                ('actor_fav', models.BooleanField(default=True)),
            ],
        ),
    ]

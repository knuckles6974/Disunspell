# Generated by Django 4.0.6 on 2022-08-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtoms', '0006_actor_movie_delete_actormovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(related_name='actor', to='mtoms.movie'),
        ),
    ]
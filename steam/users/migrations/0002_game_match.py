# Generated by Django 3.2.7 on 2021-11-02 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.game')),
                ('players', models.ManyToManyField(to='users.User')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Winning_matches', to='users.user')),
            ],
        ),
    ]

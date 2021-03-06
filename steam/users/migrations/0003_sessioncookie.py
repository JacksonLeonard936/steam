# Generated by Django 3.2.7 on 2022-01-18 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_game_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionCookie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.CharField(max_length=16, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='session_cookies', to='users.user')),
            ],
        ),
    ]

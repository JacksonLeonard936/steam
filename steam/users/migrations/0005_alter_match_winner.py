# Generated by Django 3.2.7 on 2022-04-07 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_sessioncookie_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Winning_matches', to='users.user'),
        ),
    ]
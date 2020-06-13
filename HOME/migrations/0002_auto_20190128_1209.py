# Generated by Django 2.1 on 2019-01-28 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('score', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_best_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='user_best_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HOME.User'),
        ),
    ]
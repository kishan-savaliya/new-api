# Generated by Django 4.1.4 on 2022-12-29 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.CharField(choices=[('like', 'like')], max_length=100),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='userapp.post'),
        ),
    ]
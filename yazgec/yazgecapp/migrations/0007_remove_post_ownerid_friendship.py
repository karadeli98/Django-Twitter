# Generated by Django 4.0.4 on 2022-05-21 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yazgecapp', '0006_post_ownerusername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ownerId',
        ),
        migrations.CreateModel(
            name='friendShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_friends', to='yazgecapp.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acc_friends', to='yazgecapp.user')),
            ],
        ),
    ]

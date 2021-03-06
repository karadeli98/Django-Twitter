# Generated by Django 4.0.4 on 2022-05-17 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('birthOfDate', models.DateField()),
                ('userId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yazgecapp.user')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2p', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.TextField()),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.TextField()),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Peer',
        ),
    ]

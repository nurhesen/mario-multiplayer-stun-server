# Generated by Django 4.2.3 on 2023-07-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2p', '0004_rename_offer_answer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='host_uuid',
            field=models.TextField(default='ha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='host_uuid',
            field=models.TextField(default='ha'),
            preserve_default=False,
        ),
    ]

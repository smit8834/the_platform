# Generated by Django 3.2.6 on 2021-12-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taneek', '0008_auto_20211217_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_img',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

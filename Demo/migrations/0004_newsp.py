# Generated by Django 4.2.7 on 2023-12-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0003_aboutp'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=10)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]

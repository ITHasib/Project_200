# Generated by Django 2.2.7 on 2021-06-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('athour', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]

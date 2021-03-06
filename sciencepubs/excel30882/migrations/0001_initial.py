# Generated by Django 3.0.3 on 2020-02-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicationCategoryId', models.IntegerField()),
                ('PublicationCategoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationName', models.CharField(max_length=256)),
                ('publicationIssn', models.CharField(max_length=9)),
                ('publicationEissn', models.CharField(max_length=9)),
                ('publicationName2', models.CharField(max_length=256)),
                ('publicationIssn2', models.CharField(max_length=9)),
                ('publicationEissn2', models.CharField(max_length=9)),
                ('PublicationPoints', models.IntegerField()),
                ('PublicationCategories', models.ManyToManyField(blank=True, to='excel30882.PublicationCategory')),
            ],
        ),
    ]

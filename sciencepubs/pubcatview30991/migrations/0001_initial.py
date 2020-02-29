# Pozdrawiam, DG

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

    ]

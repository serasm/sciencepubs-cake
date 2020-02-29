# Tez pozdro, DG

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubcatview30991', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublicationCategory',
        ),
    ]

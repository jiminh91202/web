# Generated by Django 4.2.7 on 2023-11-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_brand_id_alter_motorbike_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

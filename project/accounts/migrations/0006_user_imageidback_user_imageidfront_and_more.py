# Generated by Django 4.1.2 on 2022-12-01 12:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_transaction_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imageIDBack',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='user',
            name='imageIDFront',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='code',
            field=models.CharField(default=uuid.UUID('baa8b942-7175-11ed-bcdb-4851b7b990fa'), max_length=50),
        ),
    ]
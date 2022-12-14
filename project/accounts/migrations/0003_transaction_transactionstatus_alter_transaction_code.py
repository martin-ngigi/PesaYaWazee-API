# Generated by Django 4.1.2 on 2022-12-01 10:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_alter_user_status_transaction_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='TransactionStatus',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='code',
            field=models.CharField(default=uuid.UUID('a6638aea-7165-11ed-a87e-4851b7b990fa'), max_length=50),
        ),
    ]

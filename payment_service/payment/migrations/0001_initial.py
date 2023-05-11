# Generated by Django 4.1.6 on 2023-05-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerId', models.IntegerField(default=0)),
                ('sellerId', models.IntegerField(default=0)),
                ('payat', models.CharField(max_length=255)),
                ('cartId', models.IntegerField(default=0)),
                ('numberOfItem', models.IntegerField(default=0)),
                ('cost', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
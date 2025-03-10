# Generated by Django 5.0.6 on 2024-06-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_userregister_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=3)),
                ('proid', models.CharField(max_length=3)),
                ('add', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('qty', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=6)),
                ('totalprice', models.CharField(max_length=6)),
                ('paytype', models.CharField(max_length=50)),
                ('orderid', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

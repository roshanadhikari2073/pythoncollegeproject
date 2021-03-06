# Generated by Django 2.2.1 on 2019-08-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('userimage', models.ImageField(default='default.jpg', upload_to='story/')),
                ('vegetable', models.CharField(max_length=180)),
                ('phonenumber', models.CharField(max_length=10)),
                ('image', models.ImageField(default='default.jpg', upload_to='story/')),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField(max_length=20)),
                ('quantity', models.IntegerField(max_length=20)),
                ('chatroom', models.CharField(max_length=100)),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Address')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Seller',
                'ordering': ['-date'],
            },
        ),
    ]

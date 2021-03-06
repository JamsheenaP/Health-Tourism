# Generated by Django 3.1.7 on 2021-04-18 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=15)),
                ('role', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=14)),
                ('cvv', models.IntegerField()),
                ('expiry', models.CharField(max_length=7)),
                ('booking_date', models.CharField(max_length=14)),
                ('slots', models.CharField(max_length=10)),
                ('copies', models.IntegerField()),
                ('amount', models.FloatField()),
                ('order_date', models.DateField(default='2020-01-01')),
                ('status', models.IntegerField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.login')),
            ],
        ),
    ]

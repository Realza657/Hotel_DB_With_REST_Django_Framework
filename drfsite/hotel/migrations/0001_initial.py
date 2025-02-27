# Generated by Django 5.1.4 on 2025-01-11 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('staff', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('surcharges', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAuthorization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.client')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAuthorization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOfEmployment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_hired', models.DateField()),
                ('date_fired', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.position')),
            ],
        ),
        migrations.CreateModel(
            name='NeedsByPosition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.position')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.position'),
        ),
        migrations.CreateModel(
            name='AccountAccommodation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.agreement')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.agreement')),
            ],
        ),
        migrations.CreateModel(
            name='ListOfServices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.service')),
                ('service_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.serviceaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('arrived', models.BooleanField()),
                ('start_hour', models.IntegerField()),
                ('end_hour', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-27 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('established', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InkReserviorTypes',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('reservior_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NibColors',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NibPoints',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('point', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NibSizes',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nibs',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nib_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibcolors')),
                ('nib_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.brands')),
                ('nib_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibpoints')),
                ('nib_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibsizes')),
            ],
        ),
        migrations.CreateModel(
            name='InkReserviors',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('reservior_model_name', models.CharField(max_length=50)),
                ('reservior_capacity', models.FloatField()),
                ('reservior_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.inkreserviortypes')),
            ],
        ),
        migrations.CreateModel(
            name='FountainPens',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('pen_model', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.brands')),
                ('ink_reservior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.inkreserviors')),
                ('nib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibs')),
                ('supported_nib_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibsizes')),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-27 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fountainpens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('established', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FountainPen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pen_model', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.brand')),
            ],
        ),
        migrations.CreateModel(
            name='InkReservior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservior_model_name', models.CharField(max_length=50)),
                ('reservior_capacity', models.FloatField()),
                ('reservior_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.brand')),
            ],
        ),
        migrations.CreateModel(
            name='InkReserviorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservior_type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NibColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NibPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NibSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='fountainpens',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='fountainpens',
            name='ink_reservior',
        ),
        migrations.RemoveField(
            model_name='fountainpens',
            name='nib',
        ),
        migrations.RemoveField(
            model_name='fountainpens',
            name='supported_nib_size',
        ),
        migrations.RemoveField(
            model_name='inkreserviors',
            name='reservior_type',
        ),
        migrations.RemoveField(
            model_name='nibs',
            name='nib_color',
        ),
        migrations.RemoveField(
            model_name='nibs',
            name='nib_manufacturer',
        ),
        migrations.RemoveField(
            model_name='nibs',
            name='nib_point',
        ),
        migrations.RemoveField(
            model_name='nibs',
            name='nib_size',
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='FountainPens',
        ),
        migrations.DeleteModel(
            name='InkReserviors',
        ),
        migrations.DeleteModel(
            name='InkReserviorTypes',
        ),
        migrations.DeleteModel(
            name='NibColors',
        ),
        migrations.DeleteModel(
            name='NibPoints',
        ),
        migrations.DeleteModel(
            name='Nibs',
        ),
        migrations.DeleteModel(
            name='NibSizes',
        ),
        migrations.AddField(
            model_name='nib',
            name='nib_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibcolor'),
        ),
        migrations.AddField(
            model_name='nib',
            name='nib_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.brand'),
        ),
        migrations.AddField(
            model_name='nib',
            name='nib_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibpoint'),
        ),
        migrations.AddField(
            model_name='nib',
            name='nib_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibsize'),
        ),
        migrations.AddField(
            model_name='inkreservior',
            name='reservior_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.inkreserviortype'),
        ),
        migrations.AddField(
            model_name='fountainpen',
            name='ink_reservior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.inkreservior'),
        ),
        migrations.AddField(
            model_name='fountainpen',
            name='nib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nib'),
        ),
        migrations.AddField(
            model_name='fountainpen',
            name='supported_nib_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fountainpens.nibsize'),
        ),
    ]

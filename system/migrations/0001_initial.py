# Generated by Django 4.2.5 on 2023-10-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('alcalde', models.CharField(max_length=250)),
                ('imagen', models.ImageField(null=True, upload_to='type/')),
                ('votos', models.IntegerField()),
            ],
        ),
    ]

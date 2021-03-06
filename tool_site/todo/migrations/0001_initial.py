# Generated by Django 2.1.2 on 2019-01-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dateCreated', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('1', 'P1'), ('2', 'P2'), ('3', 'P3')], default='1', max_length=3)),
                ('status', models.CharField(choices=[('ND', 'Non débuté'), ('EC', 'En cours'), ('T', 'Terminé')], default='ND', max_length=10)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('finishDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.Type'),
        ),
    ]

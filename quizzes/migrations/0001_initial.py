# Generated by Django 3.1.2 on 2020-11-09 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_column='category_name', max_length=255)),
                ('order', models.IntegerField(db_column='order')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Era',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('era', models.CharField(db_column='era', max_length=255)),
                ('order', models.IntegerField(db_column='order')),
            ],
            options={
                'db_table': 'eras',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(db_column='level', max_length=100)),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(db_column='question', max_length=500)),
                ('answer', models.CharField(db_column='answer', max_length=300)),
                ('order', models.IntegerField(db_column='order')),
                ('status', models.IntegerField(db_column='status')),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.PROTECT, to='quizzes.category')),
                ('era_id', models.ForeignKey(db_column='era_id', on_delete=django.db.models.deletion.PROTECT, to='quizzes.era')),
                ('level_id', models.ForeignKey(db_column='level_id', on_delete=django.db.models.deletion.PROTECT, to='quizzes.level')),
            ],
            options={
                'db_table': 'quizzes',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='era_id',
            field=models.ForeignKey(db_column='era_id', on_delete=django.db.models.deletion.PROTECT, to='quizzes.era'),
        ),
    ]

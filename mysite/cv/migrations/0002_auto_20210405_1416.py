# Generated by Django 3.1.7 on 2021-04-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Rubric')),
            ],
            options={
                'verbose_name': 'Rubric',
                'verbose_name_plural': 'Rubrics',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bd',
            options={'ordering': ['-level'], 'verbose_name': 'Fact', 'verbose_name_plural': 'Facts'},
        ),
        migrations.AlterField(
            model_name='bd',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='fact',
            field=models.CharField(max_length=50, verbose_name='Fact'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='level',
            field=models.FloatField(blank=True, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publicate'),
        ),
        migrations.AddField(
            model_name='bd',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cv.rubric', verbose_name='Rubric'),
        ),
    ]

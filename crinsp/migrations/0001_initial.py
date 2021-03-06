# Generated by Django 2.2.5 on 2019-09-29 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testing_Date', models.DateField()),
                ('Testing_Shift', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('Rolling_Mill', models.CharField(choices=[('RSM', 'RSM'), ('URM', 'URM')], default='RSM', max_length=3)),
                ('Rail_Section', models.CharField(choices=[('UIC-60', 'UIC-60'), ('IRS-52', 'IRS-52')], default='UIC-60', max_length=6)),
                ('Testing_Result', models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail')], default='Pass', max_length=4)),
                ('IE_Testing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Heat_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heat_Number', models.CharField(max_length=6)),
                ('Testing_Detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crinsp.Testing')),
            ],
        ),
    ]

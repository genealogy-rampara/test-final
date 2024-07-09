# Generated by Django 4.2.13 on 2024-06-27 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_contactmessage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spouseinfo',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person'),
        ),
        migrations.AlterField(
            model_name='spouseinfo',
            name='spouse_fathername',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spouseinfo',
            name='spouse_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spouseinfo',
            name='spouse_village',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-17 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrato',
            name='movimentacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.transferencia'),
        ),
    ]
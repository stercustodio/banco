# Generated by Django 4.0.6 on 2022-07-17 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_alter_extrato_movimentacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrato',
            name='conta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.conta'),
        ),
    ]

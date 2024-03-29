# Generated by Django 3.2.4 on 2021-06-02 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionavisos', '0002_auto_20210602_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=240)),
                ('direccion', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='evento',
            name='email_destinatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destinatario', to='gestionavisos.direccionemail'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='email_remitente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Remitente', to='gestionavisos.direccionemail'),
        ),
    ]

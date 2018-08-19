# Generated by Django 2.0.8 on 2018-08-19 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vota', '0002_suggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'comentário',
                'verbose_name_plural': 'comentários',
            },
        ),
        migrations.AlterModelOptions(
            name='suggestion',
            options={'verbose_name': 'proposta', 'verbose_name_plural': 'propostas'},
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='sugges',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='suggestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sugges', to='vota.Suggestion', verbose_name='comentário'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='vota.User', verbose_name='usuário'),
        ),
    ]
